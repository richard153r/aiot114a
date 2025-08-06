# 查詢敘述的基本語法

- select 想要查詢欄位
- form 想要查詢表格
- wehre 查詢條件
- group by 分組設定
- havig 分組條件
- order by 排序設定
- limit 限制設定

## 使用子句順序

1. select 想要查詢欄位
2. form 想要查詢表格
3. wehre 查詢條件
4. group by 分組設定
5. havig 分組條件
6. order by 排序設定
7. limit 限制設定

## 指定需要的欄位

> selet 欄位名稱[,欄位名稱] form 表格名稱
>
>『*』 表示所有欄位
>『表格名稱』指定目前使用中的資料庫的表格名稱
>『,』有多個欄位需要隔開

## 數學運算

|優先順序|運算子|說明|範例|運算結果|
|-|-|-|-|-|
|1|%|餘數|7%3|1|
|1|MOD|餘數|7 MOD 3|1|
|1|*|乘法|7 * 3|21|
|1|/|除法|7/3|2.333|
|1|DIV|除(整數)|7 DIV 3|2|
|2|+|加法|7 + 3|10|
|2|-|減法|7-3|4|

> select 欄位名稱A*12,欄位名稱B+欄位名稱C
>
> from selet 欄位名稱[,欄位名稱] form 表格名稱

## 別名

``` SQL
select {欄位|資料|運算式} [as] [別名]
from 表格名稱;

例:select 欄位名稱A as Fidlds;
from 表格名稱;
```

## 條件查詢

> select ... from ... where 查詢條件

### 比較運算子

|運算子|說明|
|-|-|
|=|等於|
|<=>|等於|
|!=|不等於|
|<|小於|
|<=|小於等於|
|>|大於|
|>=|大於等於|

### 邏輯運算子

|運算子|說明|
|-|-|
|NOT|不是|
|&&|而且|
|AND|而且|
|&#124;&#124;|或|
|OR|或|
|XOR|互斥|

### 其他條件運算

|運算子|說明|
|-|-|
|between...and...|比較範圍|
|in(...)|比較成員|
|is|是...|
|is not|不是...|
|like|像...|

> 『between...and...』用來執行一個指定範圍條件的設定
>
> 『in(...)』使用在一組成員資料的比對條件設定

---

## 合併資料庫

### 1. 垂直合併 `union/union all`

用途：將兩個或多個 查詢結果上下合併（表結構相同），就像是把多張表或多筆結果接在一起。

``` sql
語法：
select column1, column2 from table1
union
select column1, column2 from table2;
```

|合併方式|是否去除重複|是否排序|效能|
|-|-|-|-|
|`UNION`|✅是|✅是|較慢|
|`UNION ALL`|❌否|❌否|較快|

### 2. 水平合併 `JOIN` 系列

用途：將兩張表 橫向合併（根據關聯欄位，如 ID），像是合併表格的欄位資料。

#### 2-1. `INNER JOIN` 只保留『兩邊都有匹配資料』的列

```sql
select * from table1
inner join table2 on table1.id = table2.id;
```

#### 2-2. `LEFT JOIN` 保留左邊表的『所有資料』，右邊沒有的補 null

```sql
select * from  table1
left join table2 on table1.id = table2.id;
```

#### 2-3. `RIGHT JOIN` 保留右邊表的『所有資料』，左邊沒有的補 null

```sql
select * from table1
right join table2 on table1.id = table2.id;
```

### 3. 特殊合併技巧

#### 3-1. 子查詢合併

```sql
select name, 
(select dept_name from departments where id = employees.dept_id) as department
from employees;
```

#### 3-2. INSERT INTO ... SELECT ➡️ 合併資料進一個表

```sql
insert into new_table (id, name)
select id, name from old_table;
```

|合併方式|關鍵字|用途|是否支援|
|-|-|-|-|
|垂直合併|`UNION`|合併查詢結果（去重）|✅|
|垂直合併|`UNION ALL`|合併查詢結果（含重）|✅|
|水平合併|`INNER JOIN`| 關聯欄位皆存在|✅|
|水平合併|`LEFT JOIN`| 保留左表全部資料|✅|
|水平合併|`RIGHT JOIN`| 保留右表全部資料| ✅|
|水平合併|`FULL JOIN`| 保留所有資料|❌(用UNION模擬)|
|特殊合併|子查詢|表中欄位動態對應查詢|✅|
|特殊合併|`INSERT ... SELECT`|插入合併資料到表中|✅|

---

![A1.1.SQL_Joins圖解](https://raw.githubusercontent.com/richard153r/pic/main/pic/A1.1.SQL_Joins圖解.jpg)

---

## 運算是與函式

### 值與運算式

- 數值
  - 整數:沒有小數的數字
  - 小數:包含小數的數字
- 字串值
- 日期與時間值
  - year 年
  - quarter 季
  - month 月
  - day 日
  - hour 時
  - nimute 分
  - second 秒
- NULL值

### 函式

- 字串函式

  |函數名稱|說明|
  |-|-|
  |`LOWER(字串)` |將字串轉換為小寫|
  |`UPPER(字串)`|將字串轉換為大寫|
  |`LPAD(字串1, 長度, 字串2)`|將字串1的長度擴展到指定的長度（左邊填充字串2）|
  |`RPAD(字串1, 長度, 字串2)`|將字串1的長度擴展到指定的長度（右邊填充字串2）|
  |`LTRIM(字串)` |刪除字串左邊的空格|
  |`RTRIM(字串)` |刪除字串右邊的空格|
  |`TRIM(字串)`|刪除字串兩邊的空格|
  |`REPEAT(字串, 個數)`|將字串重複指定的次數|
  |`REPLACE(字串1, 字串2, 字串3)`|將字串1中的所有字串2替換為字串3
  |`LEFT(字串, 長度)`|從字串的最左邊開始，截取指定長度的字串|
  |`RIGHT(字串, 長度)`|從字串的最右邊開始，截取指定長度的字串|
  |`SUBSTRING(字串, 位置)`|從字串的指定位置開始，截取到字串的結尾|
  |`SUBSTRING(字串, 起始位置, 長度)`|從字串的指定位置開始，截取指定長度的字串|
  |`CONCAT(字串1, 字串2, ...)`|將多個字串連接在一起，並返回一個新的字串|
  |`CONCAT_WS(分隔符, 字串1, 字串2, ...)`|使用指定的分隔符將多個字串連接在一起|
  |`length(字串)`|返回字串的字元數（即字串的長度，包含空格）|
  |`char_length(字串)`|返回字串的字符長度（與 `length` 類似，但有些資料庫可能會處理多字節字符有區別）|
  |`locate(子字串, 字串)`|返回子字串在字串中的首次出現位置（從 1 開始）|

- 數學函式

  |函式名稱|說明|
  |-|-|
  |`round(數字)`|將數字四捨五入至最接近的整數|
  |`round(數字, 位數)`|將數字四捨五入到指定的小數位數|
  |`ceil(數字)` / `ceiling(數字)`|將數字進位為最小的整數|
  |`floor(數字)`|將數字捨去為最大的整數（向下取整）|
  |`truncate(數字, 位數)`|去除數字的小數部分，僅保留指定小數位數的數字|
  |`pi()`|返回圓周率 π 的值|
  |`pow(數字1, 數字2)` / `power(數字1, 數字2)`|返回 `數字1` 的 `數字2` 次方|
  |`rand()` |生成一個介於 0 和 1 之間的隨機數字|
  |`sqrt(數字)`|返回數字的平方根|

- 日期時間函式

  |函式名稱|說明|
  |-|-|
  |`now()`|返回當前的日期和時間|
  |`curdate()`|返回當前的日期（不包含時間）|
  |`curtime()`|返回當前的時間（不包含日期）|
  |`year(日期)`|提取日期中的年份部分|
  |`month(日期)`提取日期中的月份部分|
  |`day(日期)`|提取日期中的日部分|
  |`monthname(日期)`|返回日期所對應的月份名稱|
  |`dayname(日期)`|返回日期所對應的星期幾名稱|
  |`datediff(d1, d2)`|返回兩個日期之間的差值，單位為天數|
  |`dayofweek(日期)`|返回日期是星期幾，1=星期日，7=星期六|
  |`dayofyear(日期)`|返回日期是當年的第幾天|
  |`quarter(日期)`|返回日期所對應的季度，1 = 第一季度，2 = 第二季度|
  |`extract(單位 from 日期/時間)`|從日期或時間中提取指定單位的數值|
  |`hour(時間)`|提取時間中的小時部分|
  |`minute(時間)`|提取時間中的分鐘部分|
  |`second(時間)`|提取時間中的秒數部分|

- 流程控制函式

  |函數/語法|功能說明|用途|
  |-|-|-|
  |`if()`|單一條件判斷，兩個選項的流程控制|判斷「是/否」、「真/假」的簡單邏輯|
  |`case`|多重條件判斷，類似多層 if- |複雜多條件的流程判斷|
  
  > if(條件, 運算式1, 運算式2):如果「條件」成立（為真），就回傳「運算式1」；否則回傳「運算式2」

    ```sql
    SELECT ename,
        IF(sal > 50000, '高薪', '低薪') AS 薪資等級
    FROM employees;
    ```

  > CASE 表達式:根據多個條件逐一判斷，符合哪個條件就回傳對應的結果，類似多重 if-else

  ```sql
    SELECT ename,
       CASE 
         WHEN sal > 100000 THEN '非常高薪'
         WHEN sal > 50000 THEN '高薪'
         ELSE '低薪'
       END AS 薪資等級
    FROM employees;
  ```

- 其他函式

    |函數名稱|說明|
    |-|-|
    |`ifnull(參數, 運算式)`|如果「參數」是 `NULL`，則回傳「運算式」，否則回傳「參數」本身。常用來替代 NULL 值|
    |`isnull(參數)`|判斷「參數」是否為 `NULL`，是則回傳 `1`（真），否則回傳 `0`（假）|

---

## 群組查詢

### 群組函式

   |函數名稱|說明|
   |-|-|
   |max()|找出欄位中的最大值|
   |min()|找出欄位中的最小值|
   |sum()|計算欄位數值的總和|
   |avg()|計算欄位數值的平均值|

### group_concat函式

- `group_concat()` 是一個聚合函式，用來**將同一組（GROUP BY）中多筆資的欄位值串接成一個字串**，常用於將多筆資料合併成清單顯示。
  - 通常會以逗號 , 分隔不同的值，也可自訂分隔符號。
  - 可以使用 ORDER BY 子句，決定串接時的排序。
  
 ```sql
 SELECT 部門編號,GROUP_CONCAT(員工姓名 ORDER BY 員工姓名 SEPARATOR ',') AS 員工名單
 FROM employees
 GROUP BY 部門編號;
 ```

- ORDER BY 員工姓名：串接前先依姓名排序
- SEPARATOR ', '：指定用逗號+空格分隔

### group by 與 having 子句

#### group by 子句

- GROUP BY 是用來 依指定欄位分組，把同類型資料歸類在一起。
- 常用來配合聚合函數（SUM、COUNT、AVG 等）做統計。
  
  ```sql
  SELECT 欄位1, 聚合函數(欄位2)
  FROM 表名
  GROUP BY 欄位1;
  ```

- 非聚合欄位必須在 GROUP BY 中出現。
- GROUP BY 不會排序，排序要用 ORDER BY。
- 可以分多欄位組合分組：GROUP BY 欄位1, 欄位2。

#### having 子句

- WHERE 是針對 原始資料 進行篩選
- HAVING 是針對 分組（GROUP BY）後的結果 進行篩選

```sql
SELECT ...
FROM ...
WHERE 查詢條件 //可使用子查詢
GROUP BY 分組設定
HAVING 分組條件 //可使用子查詢
```

✅ WHERE vs HAVING 差異比較

|用法|篩選對象|什麼時候執行|範例|
|-|-|-|-|
|`WHERE`|原始每筆資料|在分組 **前** 篩選 |`WHERE sal > 10000`|
|`HAVING`|分組後的聚合資料|在分組 **後** 篩選| `HAVING AVG(sal) > 20000`|

#### 比較運算子(子查詢)

只要是設定的資料需要先執行查詢後才可以得到，就應該要使用子查詢

子查詢敘述回傳的資料是用來與前面的資料執行判斷比較用的，所以最多只能回傳一筆紀錄，而且只能有一個欄位的資料

---
