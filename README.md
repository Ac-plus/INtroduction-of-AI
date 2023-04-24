# 产生式系统的设计与实现

---

## **一、实验内容**

本次实验要求实现一个动物识别系统，即完成识别虎、金钱豹、斑马、长颈鹿、鸵鸟、企鹅、信天翁等七种动物的产生式系统。实验需要实现一个“专家系统”程序，用户输入一系列已知的动物特征，然后程序根据规则库来判断并输出用户所描述的是什么动物。

 

## **二、实验原理与步骤**

### **2.1** **实验原理**

#### 2.1.1 产生式系统

如图2-1所示，产生式系统控制着一个规则库、一个推理机和一个综合数据库。其中规则库内存放用户输入信息与识别出的内容的匹配规则，经过综合数据库和推理机的分析与处理，最终能够得到较为准确的输出。

![img](file:///C:/Users/CMJ/AppData/Local/Temp/msohtmlclip1/01/clip_image002.png)

图2-1 产生式系统的基本结构

 

#### 2.1.2 动物识别系统规则库

```
R1： IF  该动物有毛发  
   THEN 该动物是哺乳动物
R2： IF  该动物有奶   
   THEN 该动物是哺乳动物
R3： IF  该动物有羽毛  
   THEN 该动物是鸟
R4： IF  该动物会飞     AND 会下蛋 
   THEN 该动物是鸟
R5： IF  该动物吃肉   
   THEN 该动物是食肉动物
R6： IF  该动物有犬齿   AND 有爪     AND 眼盯前方
   THEN 该动物是食肉动物
R7： IF  该动物是哺乳动物 AND 有蹄 
   THEN 该动物是有蹄类动物
R8： IF  该动物是哺乳动物 AND 是反刍动物 
   THEN 该动物是有蹄类动物
R9 ： IF 该动物是哺乳动物  AND 是食肉动物  AND 是黄褐色 AND 身上有暗斑点   
   THEN 该动物是金钱豹                   
R10：IF 该动物是哺乳动物   AND 是食肉动物 AND 是黄褐色 AND 身上有黑色条纹  
   THEN 该动物是虎                   
R11： IF  该动物是有蹄类动物 AND 长脖子    AND 有长腿 AND 身上有暗斑点   
   THEN 该动物是长颈鹿                   
R12：IF 该动物有蹄类动物  AND 身上有黑色条纹 
   THEN 该动物是斑马
R13：IF 该动物是鸟     AND 有长脖子  AND  有长腿  AND 不会飞    AND 有黑白二色    
   THEN 该动物是鸵鸟
R14： IF 该动物是鸟    AND 会游泳    AND  不会飞 AND 有黑白二色    
   THEN 该动物是企鹅             
R15： IF 该动物是鸟    AND 善飞        
   THEN 该动物是信天翁
```



 

#### 2.1.3 动物识别系统算法设计

（1）系统基本框架

如图2-2所示，根据条件和规则库里的规则判断是否匹配，然后以R1，R2，…的顺序依次进行匹配，如果匹配成功则执行该规则，否则匹配下一条，直至结束。这样就可以得到所寻找的是哪一种动物。

![img](file:///C:/Users/CMJ/AppData/Local/Temp/msohtmlclip1/01/clip_image004.png)

图2-2 动物识别系统工作流程图

（2）反向推理机制

如果用户输入的信息不完整，则系统需要进行确认和反向推理。这种情况下的算法设计如图2-3所示。可见如果条件提供不全，系统会返回寻找符合程度最高的可能结果，并逐步询问用户更明确的条件，更新符合程度，最后输出正确结果。

![img](file:///C:/Users/CMJ/AppData/Local/Temp/msohtmlclip1/01/clip_image006.png)

图2-3 反向推理算法流程图

（3）实例理论分析

如图2-4所示是利用上述流程对“长颈鹿”进行匹配的过程。从产奶和有蹄开始会逐步向上推理，得到哺乳动物、有蹄类动物，最后得到长颈鹿。

由此可见，该算法流程在理论上可以准确地实现动物识别的功能。

![img](file:///C:/Users/CMJ/AppData/Local/Temp/msohtmlclip1/01/clip_image008.png)

图2-4 长颈鹿的推理过程

 

   **2.2** **实验步骤**

#### 2.2.1 实验环境配置

（1）实验环境：Windows10+MinGW32

（2）程序语言：C++

（3）编译系统：g++ 6.3.0

（4）输入方式：用户逐步输入

 

#### 2.2.2 实验操作步骤

根据2.1和2.2.1等部分的描述，本实验的具体步骤如下：

（1）配置实验环境；

（2）分析问题需求；

（3）设计动物识别系统的算法，画出流程图，分析伪代码；

（4）根据流程图编写完整程序；

（5）分析实验结果。

 

 

 

## **三、实验结果及分析**

### **3.1** **正常识别**

  （1）首先根据图2-3所示的信息，按照**暗斑点****+****长脖****+****长腿****+****有蹄****+****产奶**的条件组合进行搜索，成功得到“长颈鹿”的结果，如图3-1所示。

![img](file:///C:/Users/CMJ/AppData/Local/Temp/msohtmlclip1/01/clip_image010.png)

图3-1

（2）之后变换搜索条件，使用**暗斑点****+****长脖****+****长腿****+****蹄类**的条件组合进行搜索，也能成功得到“长颈鹿”的结果，如图3-2所示。

![img](file:///C:/Users/CMJ/AppData/Local/Temp/msohtmlclip1/01/clip_image012.png)

图3-2

### **3.2** **反向推理**

  下面进行输入信息不完整时，观察系统的行为。按照**有毛****+****会飞****+****能下蛋**的条件组合输入，程序会显示输入不完整，并依次提示用户输入该动物是否具有善飞、食肉、有爪、有暗斑点、有黑色条纹、会游泳和长脖的特点。在依次输入准确信息（Yes或No）后，程序得到正确的结果“信天翁”。

![img](file:///C:/Users/CMJ/AppData/Local/Temp/msohtmlclip1/01/clip_image014.png)

图3-3

### **3.3** **识别范围超限**

下面模拟识别范围超限时系统的行为。同样按照**有毛****+****会飞****+****能下蛋**的条件组合输入，程序会显示输入不完整，并依次提示用户输入后续信息。

![img](file:///C:/Users/CMJ/AppData/Local/Temp/msohtmlclip1/01/clip_image016.png)

图3-4

如图3-4所示，在依次输入准确信息（Yes或No）后，程序认为无法识别该动物，因为其不在给定的规则库里，但也给出了其可能的物种，即鸟类或哺乳类。

 

### **3.4** **结果分析**

根据本次实验，总结出了所设计的动物识别系统的一些特点，如下表所示。

表1 产生式系统的优缺点归纳



| 产生式动物识别系统 |                    |                                                              |                                                              |
| ------------------ | ------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 序号               | 归纳               | 说明                                                         |                                                              |
| 优点               | 1                  | 方法更自然                                                   | 所设计的系统按照人们思考的常规思路进行推理，方便理解         |
| 2                  | 功能模块化         | 每条规则及其后续均有较强的联系，且能将动物划分为不同的物种   |                                                              |
| 3                  | 有效               | a.所设计的系统能准确识别出每一种规则库里有的动物  b.无法识别时能准确判断原因，如输入有误、规则不足等 |                                                              |
| 4                  | 表达更清晰         | a.整体的框架清晰明确  b.查询时，程序给出的思路明确，会让用户逐步输入信息 |                                                              |
| 缺点               | 1                  | 效率较低                                                     | a.查询时需要逐步匹配动物特征，所消耗的时间更长  b.如果中间某步规则无法匹配，则需要重新遍历规则库 |
| 2                  | 无法表达结构性知识 | 无                                                           |                                                              |

 

## **四、实验结论及心得体会**



### **4.1** **实验结论**

本实验中，通过启发式搜索和反向推理等方法，实现了对动物识别系统的模拟与设计实现，能够识别 规则库内的所有动物，并对不同的错误（输入编号超限、所描述的动物不在规则库内等）进行相应反应与输出。综上所述，本次实验大体成功。

 

### **4.2** **心得体会**

本次实验要求我们对专家系统进行实现，实际上是考察我们将课堂上所学的产生式系统的知识进行实际运用。在编写代码的过程中，我也遇到了许多困难，例如代码量庞大导致前后思路不连贯、调试过程中动物的输出不符合预期等，后来在经过一段时间的debug之后解决了这些问题。

通过这次的实验，我也认识到实践出真知的道理，只有把书上的理论知识运用到实践，才是真正地掌握。在这一过程中我们也收获了许多：实践能力、编程能力和理论联系实际的能力都有所提高。希望在今后的学习中，对人工智能和问题求解等知识的理解都能够更上一个台阶，从而提高自身的硬实力。

 ## **五、附录**

代码：

```cpp
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
```

