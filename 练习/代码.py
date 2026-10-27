import csv
import json
import os

# ===================== 1. 定义课程类 Course =====================
class Course:
    def __init__(self, course_name, credit):
        self.course_name = course_name  # 课程名称
        self.credit = credit            # 学分

    def to_dict(self):
        """对象转字典，用于json存储"""
        return {
            "course_name": self.course_name,
            "credit": self.credit
        }

    @staticmethod
    def from_dict(data):
        """字典转Course对象"""
        return Course(data["course_name"], float(data["credit"]))

# ===================== 2. 定义学生类 Student =====================
class Student:
    def __init__(self, stu_id, name, gender):
        self.stu_id = stu_id       # 学号
        self.name = name           # 姓名
        self.gender = gender       # 性别
        self.scores = {}           # 成绩字典 {课程名: 分数}

    def add_score(self, course_name, score):
        """添加/修改成绩，校验分数范围"""
        if not isinstance(score, (int, float)):
            raise ValueError("成绩必须为数字")
        if score < 0 or score > 100:
            raise ValueError("成绩范围必须在 0 ~ 100 之间")
        self.scores[course_name] = score

    def get_total_score(self):
        """计算总分"""
        return sum(self.scores.values())

    def get_avg_score(self):
        """计算平均分"""
        if len(self.scores) == 0:
            return 0.0
        return round(sum(self.scores.values()) / len(self.scores), 2)

    def is_course_pass(self, course_name):
        """判断单门课程是否及格(60分及格)"""
        if course_name not in self.scores:
            raise ValueError(f"暂无【{course_name}】成绩")
        return self.scores[course_name] >= 60

    def all_course_pass(self):
        """判断所有课程是否全部及格"""
        if not self.scores:
            return False
        return all(s >= 60 for s in self.scores.values())

    def to_dict(self):
        """对象转字典，用于存储"""
        return {
            "stu_id": self.stu_id,
            "name": self.name,
            "gender": self.gender,
            "scores": self.scores
        }

    @staticmethod
    def from_dict(data):
        """字典转Student对象"""
        stu = Student(data["stu_id"], data["name"], data["gender"])
        # 成绩转为浮点型
        stu.scores = {k: float(v) for k, v in data["scores"].items()}
        return stu

# ===================== 3. 数据持久化工具（CSV + JSON） =====================
class FileManager:
    STU_CSV = "students.csv"
    SCORE_JSON = "scores.json"

    # 保存学生信息到 students.csv
    @staticmethod
    def save_students(student_list):
        try:
            headers = ["stu_id", "name", "gender"]
            with open(FileManager.STU_CSV, "w", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=headers)
                writer.writeheader()
                for stu in student_list:
                    writer.writerow({
                        "stu_id": stu.stu_id,
                        "name": stu.name,
                        "gender": stu.gender
                    })
        except Exception as e:
            print(f"保存学生文件失败：{e}")

    # 从 students.csv 读取学生基础信息
    @staticmethod
    def load_students():
        student_list = []
        if not os.path.exists(FileManager.STU_CSV):
            return student_list
        try:
            with open(FileManager.STU_CSV, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    stu = Student(row["stu_id"], row["name"], row["gender"])
                    student_list.append(stu)
        except Exception as e:
            print(f"读取学生文件失败：{e}")
        return student_list

    # 保存所有成绩到 scores.json
    @staticmethod
    def save_scores(student_list, course_list):
        try:
            data = {
                "courses": [c.to_dict() for c in course_list],
                "student_scores": [stu.to_dict() for stu in student_list]
            }
            with open(FileManager.SCORE_JSON, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"保存成绩文件失败：{e}")

    # 从 scores.json 读取课程+学生成绩
    @staticmethod
    def load_scores():
        course_list = []
        student_list = []
        if not os.path.exists(FileManager.SCORE_JSON):
            return course_list, student_list
        try:
            with open(FileManager.SCORE_JSON, "r", encoding="utf-8") as f:
                data = json.load(f)
            # 读取课程
            for c_data in data.get("courses", []):
                course_list.append(Course.from_dict(c_data))
            # 读取学生+成绩
            for s_data in data.get("student_scores", []):
                student_list.append(Student.from_dict(s_data))
        except Exception as e:
            print(f"读取成绩文件失败：{e}")
        return course_list, student_list

# ===================== 4. 核心业务系统 =====================
class EduManager:
    def __init__(self):
        # 加载本地文件数据
        self.course_list, self.student_list = FileManager.load_scores()
        # 兼容：如果学生列表为空，再单独加载csv
        if not self.student_list:
            self.student_list = FileManager.load_students()

    # 统一保存所有数据
    def save_all(self):
        FileManager.save_students(self.student_list)
        FileManager.save_scores(self.student_list, self.course_list)

    # 根据学号查找学生
    def find_student(self, stu_id):
        for stu in self.student_list:
            if stu.stu_id == stu_id:
                return stu
        return None

    # 根据课程名查找课程
    def find_course(self, course_name):
        for c in self.course_list:
            if c.course_name == course_name:
                return c
        return None

    # -------- 1. 学生管理：添加学生 --------
    def add_student(self):
        print("----- 添加学生 -----")
        try:
            stu_id = input("请输入学生学号：").strip()
            if not stu_id:
                print("学号不能为空！")
                return
            if self.find_student(stu_id):
                print("该学号已存在！")
                return

            name = input("请输入学生姓名：").strip()
            if not name:
                print("姓名不能为空！")
                return
            gender = input("请输入学生性别：").strip()

            new_stu = Student(stu_id, name, gender)
            self.student_list.append(new_stu)
            self.save_all()
            print("✅ 学生添加成功！")
        except Exception as e:
            print(f"❌ 添加失败：{e}")

    # -------- 2. 学生管理：修改学生 --------
    def modify_student(self):
        print("----- 修改学生信息 -----")
        stu_id = input("请输入要修改的学生学号：").strip()
        stu = self.find_student(stu_id)
        if not stu:
            print("该学生不存在！")
            return
        try:
            new_name = input(f"原姓名【{stu.name}】，输入新姓名(回车不修改)：").strip()
            if new_name:
                stu.name = new_name
            new_gender = input(f"原性别【{stu.gender}】，输入新性别(回车不修改)：").strip()
            if new_gender:
                stu.gender = new_gender
            self.save_all()
            print("✅ 学生信息修改成功！")
        except Exception as e:
            print(f"❌ 修改失败：{e}")

    # -------- 3. 学生管理：删除学生 --------
    def del_student(self):
        print("----- 删除学生 -----")
        stu_id = input("请输入要删除的学生学号：").strip()
        stu = self.find_student(stu_id)
        if not stu:
            print("该学生不存在！")
            return
        self.student_list.remove(stu)
        self.save_all()
        print("✅ 学生删除成功！")

    # -------- 4. 课程管理：添加课程 --------
    def add_course(self):
        print("----- 添加课程 -----")
        try:
            c_name = input("请输入课程名称：").strip()
            if not c_name:
                print("课程名不能为空！")
                return
            if self.find_course(c_name):
                print("该课程已存在！")
                return
            credit = float(input("请输入课程学分："))
            new_course = Course(c_name, credit)
            self.course_list.append(new_course)
            self.save_all()
            print("✅ 课程添加成功！")
        except ValueError:
            print("❌ 学分必须是数字！")
        except Exception as e:
            print(f"❌ 添加失败：{e}")

    # -------- 5. 课程管理：删除课程 --------
    def del_course(self):
        print("----- 删除课程 -----")
        c_name = input("请输入要删除的课程名称：").strip()
        course = self.find_course(c_name)
        if not course:
            print("该课程不存在！")
            return
        self.course_list.remove(course)
        # 同步删除所有学生该门课成绩
        for stu in self.student_list:
            if c_name in stu.scores:
                del stu.scores[c_name]
        self.save_all()
        print("✅ 课程已删除，并同步清除相关成绩！")

    # -------- 6. 录入/修改学生成绩 --------
    def input_score(self):
        print("----- 录入/修改学生成绩 -----")
        if not self.course_list:
            print("暂无课程，请先添加课程！")
            return
        stu_id = input("请输入学生学号：").strip()
        stu = self.find_student(stu_id)
        if not stu:
            print("该学生不存在！")
            return

        print("当前已有课程：")
        for idx, c in enumerate(self.course_list, 1):
            print(f"{idx}. {c.course_name} (学分:{c.credit})")

        c_name = input("请输入要录入成绩的课程名：").strip()
        if not self.find_course(c_name):
            print("课程不存在！")
            return
        try:
            score = float(input("请输入课程成绩："))
            stu.add_score(c_name, score)
            self.save_all()
            print("✅ 成绩录入/修改成功！")
        except ValueError:
            print("❌ 成绩必须为数字！")
        except Exception as e:
            print(f"❌ 录入失败：{e}")

    # -------- 7. 查询学生成绩单（单科、总分、平均分） --------
    def query_student_score(self):
        print("----- 查询学生成绩单 -----")
        stu_id = input("请输入学生学号：").strip()
        stu = self.find_student(stu_id)
        if not stu:
            print("该学生不存在！")
            return
        print(f"\n【学生信息】学号：{stu.stu_id}  姓名：{stu.name}  性别：{stu.gender}")
        if not stu.scores:
            print("暂无任何成绩记录")
            return
        print("各科成绩：")
        for c_name, s in stu.scores.items():
            print(f"  {c_name}：{s} 分，{'及格' if stu.is_course_pass(c_name) else '不及格'}")
        print(f"👉 总分：{stu.get_total_score()} 分")
        print(f"👉 平均分：{stu.get_avg_score()} 分")
        print(f"👉 全部课程是否及格：{'是' if stu.all_course_pass() else '否'}")

    # -------- 8. 按课程统计报表：最高分、最低分、平均分、不及格人数 --------
    def course_stat(self):
        print("----- 课程成绩统计报表 -----")
        if not self.course_list:
            print("暂无课程！")
            return
        if not self.student_list:
            print("暂无学生数据！")
            return

        for course in self.course_list:
            c_name = course.course_name
            score_list = []
            fail_count = 0
            # 收集该课程所有有效成绩
            for stu in self.student_list:
                if c_name in stu.scores:
                    s = stu.scores[c_name]
                    score_list.append(s)
                    if s < 60:
                        fail_count += 1
            if not score_list:
                print(f"\n【{c_name}】暂无学生成绩")
                continue

            max_s = max(score_list)
            min_s = min(score_list)
            avg_s = round(sum(score_list) / len(score_list), 2)
            max_names = [stu.name for stu in self.student_list if stu.scores.get(c_name, -1) == max_s]
            min_names = [stu.name for stu in self.student_list if stu.scores.get(c_name, -1) == min_s]

            print(f"\n==== {c_name} 统计 ====")
            print(f"最高分：{max_s} 分  学生：{','.join(max_names)}")
            print(f"最低分：{min_s} 分  学生：{','.join(min_names)}")
            print(f"平均分：{avg_s} 分")
            print(f"不及格人数：{fail_count} 人")

    # -------- 9. 按学生总分降序排序 --------
    def sort_by_total(self):
        print("----- 按学生总分排序（从高到低） -----")
        if not self.student_list:
            print("暂无学生数据！")
            return
        # 按总分降序排序
        sorted_stus = sorted(self.student_list, key=lambda x: x.get_total_score(), reverse=True)
        print("排名\t学号\t姓名\t总分\t平均分")
        print("-" * 50)
        for idx, stu in enumerate(sorted_stus, 1):
            total = stu.get_total_score()
            avg = stu.get_avg_score()
            print(f"{idx}\t{stu.stu_id}\t{stu.name}\t{total}\t{avg}")

    # -------- 10. 展示所有学生 --------
    def show_all_student(self):
        print("----- 全部学生列表 -----")
        if not self.student_list:
            print("暂无学生信息！")
            return
        for idx, stu in enumerate(self.student_list, 1):
            print(f"{idx}. 学号：{stu.stu_id} 姓名：{stu.name} 性别：{stu.gender}")

    # -------- 主菜单 --------
    def main_menu(self):
        menu = """
==================== 教务管理系统 ====================
1. 添加学生        2. 修改学生信息     3. 删除学生
4. 添加课程        5. 删除课程        6. 录入/修改成绩
7. 查询学生成绩单  8. 课程成绩统计报表 9. 按总分排序学生
10. 查看所有学生   0. 退出系统
======================================================
        """
        while True:
            print(menu)
            try:
                choice = input("请输入功能编号(0-10)：").strip()
                if choice == "0":
                    print("👋 退出系统，数据已自动保存！")
                    break
                elif choice == "1":
                    self.add_student()
                elif choice == "2":
                    self.modify_student()
                elif choice == "3":
                    self.del_student()
                elif choice == "4":
                    self.add_course()
                elif choice == "5":
                    self.del_course()
                elif choice == "6":
                    self.input_score()
                elif choice == "7":
                    self.query_student_score()
                elif choice == "8":
                    self.course_stat()
                elif choice == "9":
                    self.sort_by_total()
                elif choice == "10":
                    self.show_all_student()
                else:
                    print("⚠️ 输入无效，请选择 0~10 之间的数字！")
            except Exception as e:
                print(f"⚠️ 程序异常：{e}")

# ===================== 程序入口 =====================
if __name__ == "__main__":
    app = EduManager()
    app.main_menu()