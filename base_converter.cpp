#include<iostream>
#include<bitset>
#include<cstdint>
#include<string>
#include<string_view>
int My二_十(std::string shuzi);
int My绝对();
int My十_二(std::uint64_t x);
int My验证(int x); 
void My中断();
std::uint8_t k{};
int main()
{
	std::cout << "十进制转二进制（键入1）或者二进制转十进制（键入0）？\n";
	std::uint16_t t{};
	std::cin >> t;
	if (t == 1)
	{
		int s{};
		std::cout << "输入十进制\n";
		s = { My绝对() };
		s = { My验证(s) };
		My十_二(static_cast<std::uint64_t>(s));
		My中断();
	}
	else if (t == 0)
	{
		std::string shuzi{};
		std::cout << "输入二进制\n";
		std::getline(std::cin >> std::ws, shuzi);
		My二_十(shuzi);
		My中断();
	}
	else
	{
		std::cout << "输入有误！";
		My中断();
		return 0;
	}
	}
			
int My十_二(std::uint64_t x)
{
	std::bitset<12> y{x};
	std::cout << y;
	return 0;
}
int My二_十(std::string shuzi)
{

	std::bitset<12> x{ shuzi };
	unsigned long long p{ x.to_ulong() };
	if (shuzi.length() <= 12)
	{
		std::cout << p << std::endl;
	}
	else
	{
		std::cout << "超过计算范围！\n";
	}
		return 0;
}
int My绝对()
{
	int s{};
	std::cin >> s;
	s = { (s > 0) ? s : (-s) };
	return s;
}
int My验证(int x)
{
	if (x <= 4095)
		return x;
	else
	{
		std::cout << "超过计算范围！\n";
		return 0;
	}
}
void My中断()
{
	std::cin >> k;
}
