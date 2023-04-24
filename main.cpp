#include <iostream>
#include <iomanip>
#include <string>
using namespace std;
int RULENUM=15;//动物识别系统的规则库有条规则
int CAUSENUM=5;//各条规则中的前提条件最多有个
int count = 0;//记录所选择的动物特征的个数
/*事实*/
string fact[] ={ "", "有毛发", "有奶", "有羽毛", "会飞", "会下蛋", "吃肉", "有犬齿", "有爪","眼盯前方", "有蹄", "嚼反刍", "黄褐色", "身上有暗斑点", "身上有黑色条纹", "有长脖子","有长腿", "不会飞", "会游泳", "有黑白二色", "善飞", "哺乳动物", "鸟", "食肉动物", "蹄类动物", "金钱豹", "虎", "长颈鹿", "斑马", "鸵鸟", "企鹅", "信天翁" };
/*规则*/
int rule[][6]={{ 0, 0, 0, 0, 0, 0 },{21, 1, 0, 0, 0, 0 },{ 21, 2, 0, 0, 0, 0 }, { 22, 3, 0, 0, 0, 0 }, {22, 4, 5, 0, 0, 0 },{ 23, 6, 0, 0, 0, 0 }, { 23, 7, 8, 9, 0, 0 }, { 24, 21, 10, 0, 0, 0 }, { 24, 21, 11, 0, 0, 0 }, { 25, 21, 23, 12, 13, 0 }, { 26, 21, 23, 12, 14, 0 }, { 27, 24, 15, 16, 13, 0 }, { 28, 24, 14, 0, 0, 0 }, { 29, 22, 15, 16, 17, 19 }, { 30, 22, 18, 17, 19, 0 }, { 31, 22, 20, 0, 0, 0 } };
 
int conditionlist[24];//所选择的动物特征
 
bool match(int a);           //函数声明
int inference();
 
int main()
{
    cout<<"以下是一些动物的特征:"<<endl;
    for (int i=1;i<=24;i++)
    {
        cout<<i<<".";
        cout<<setiosflags(ios::left)<<setw(14)<<fact[i]<<"  ";
        if (i%4==0)
        {
            cout<<endl;
        }
    }
    int a;
    int k=0;
 
     cout<<"请选择动物的特征:"<<endl;
     while((cin>>a))                      //a为整形的，按任意字母可结束循环
     {
       conditionlist[k]=a;                   
       k++;
       count++;
     }
     cout<<"该动物名称为："<<endl;
     inference();
 
return 0;   
}
 
 /*知识匹配*/
bool match(int a)
{
    int i=1;
    int j=0;
    int flag=0;
    int flag1=0;
    int num=0;
    while ((flag==i-1)&&(flag1!=count))
    {   
        flag=0;
        for (i=1;i<=CAUSENUM;i++)
        {
            if (rule[a+num][i]==0)
                break;                              
            for (j=0;j<count;j++)                     //所选择的动物特征的条数
            {
         if (rule[a+num][i]==conditionlist[j])//匹配上一个条件flag计数加一
                {
                    flag++;
                    flag1++;        
                    break;
                }
            }
        }
        num++;
    }
 
    if ((flag!=i-1)||(count==0))
    {
        return false;
    }
    else
    {   
        for (i=0;i<num;i++)
        {
            for (j=0;j<num;j++)
            {
                if ((i!=j)&&(rule[a+i][0]!=rule[a+j][0]))
                {
                    return false;
                }
            }
    }
        return true;
    }
}
/*推理*/
int inference()
{
    int i;
 
    int j=0;
    for (i=1; i<=RULENUM;i++)
    {
        if (match(i)==true)
        {
            cout<<fact[rule[i][0]]<<endl;
            return 0;
        }
 
    }
    cout<<"未知动物"<<endl;
    return 0;
 }
