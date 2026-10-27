from circle_fun import *
print("==========计算披萨成本=========")

s_radius=10#小号披萨
m_radius=10#中号披萨
l_radius=10#大号披萨



small_area=circle_area(s_radius)
medium_area=circle_area(m_radius)
large_area=circle_area(l_radius)

small_cost=small_area*0.5
medium_cost=medium_area*0.5
large_cost=large_area*0.5

print(f"小披萨面积是:{small_area}cm²,成本:{small_cost:.1f}元")
print(f"中披萨面积是:{medium_area}cm²,成本:{medium_cost:.1f}元")
print(f"大披萨面积是:{large_area}cm²,成本:{large_cost:.1f}元")