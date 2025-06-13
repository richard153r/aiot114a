# Sublime Text

**1. 安裝[Sublime Text](https://www.sublimetext.com/) 點選Windows 64bit 下載安裝版**

**2. 在工具 >> 瀏覽器資源包 >> 跳出資料夾後再將程式關掉**
![20250606085835](https://raw.githubusercontent.com/richard153r/pic/main/pic/20250606085835.png)
**3. 再將已有資源包，直接丟進資料夾內(就不用手動自己安裝)**
**4. 重新開啟 Sublime Text 就會看到安裝的資源包**

- 可以打一個<!>再按Tab測試 是否有跳出內容

**5. 手動新增套件**
![20250606104506](https://raw.githubusercontent.com/richard153r/pic/main/pic/20250606104506.png)

- remove 移除套件
- list 列出所以套件
- install 安裝套件

![20250606104750](https://raw.githubusercontent.com/richard153r/pic/main/pic/20250606104750.png)
安裝完成；Usage操作教學
![20250606104926](https://raw.githubusercontent.com/richard153r/pic/main/pic/20250606104926.png)

---

## HTML 常用標籤

### 1. 文字與標題

`<h1> ~ <h6>` 標題 1~6級
`<p>`  段落
`<br>` 換行
`<li>` 清單項目
`<ol>` 有序清單（編號）
`<ul>` 無序清單（bullet）
*亂文產生 lorem 按Tab*

### 2. 表格部分

- `<table>` 表格範圍
  - table中的屬性>>border框線；width寬度；align位置

- `<tr>` 表格中的列
- `<td>` 表格中的儲存格
- `<th>` 表格中的表頭標題
**快速呈現表格 `table>(tr>td*3)*4`**

### 3. 影像

- `<img src="" alt="">`
  - src >> 圖片位置；alt >> 圖片說明
  - 快速呈現多張圖片 `img[src=images/w$.jpg]*數量`  $ >> 連續編號

亂圖片產生 fakeimg 按Tab

### 4. 多媒體

|標籤|功能|常見用途|是否可提供備案內容|語法特性|支援格式|
|-|-|-|-|-|-|
|`<embed>`| 快速嵌入外部檔案|插入 PDF、影片、音訊等|❌ 不支援| 單標籤，自閉合| PDF、MP3、MP4、Flash等|
|`<object>`| 彈性嵌入外部資源，可內含備援| 嵌入 PDF、HTML、圖形等|✅ 可放備案內容|有開關標籤，可內含內容|HTML、PDF、SVG、影片、Flash等|
|`<video>`| 原生播放影片，支援控制列| 播放 MP4、WebM 影片|✅ `<source>` + 備案|有開關標籤，可內含內容 |MP4、WebM、Ogg|
|`<audio>`| 原生播放音訊，支援控制列| 播放 MP3、音效檔案|✅ `<source>` + 備案|有開關標籤，可內含內容|MP3、Ogg、WAV|

- `<embed>` 用來嵌入外部內容
- `<object>`
- `<video> 影片做法1`

    ```html
    <!--controls >> 增加手動播放鈕；
    loop >> 循環播放；
    autoplay >> 自動撥放；
    如不會撥放再加 >> muted-->
    <video src="影片位置" controls loop autoplay muted></video>
    ```

- `<video> 影片做法2`

   ```html
   <!--source >> 來源 -->
   <video controls loop autoplay muted>
        <source src="影片位置" type="video/mp4">
        <source src="影片位置" type="video/ogg">
    </video>
   ```

- `<audio> 音樂做法1`

    ```html
    <audio src="音樂位置" controls loop ></audio>
    ```

- `<audio> 音樂做法2`

   ```html
    <audio controls loop>
        <!--source >> 來源 -->
        <source src="音樂位置" type="audio/mp3">
        <source src="音樂位置" type="audio/ogg">
    </audio>
    ```

[聲音下載](https://ncs.io/?_gl=1*1ci88zi*_up*MQ..*_ga*MTc0MjQ3MzgxNi4xNzQ5MTc5NzE3*_ga_PFS54FR7NV*czE3NDkxNzk3MTYkbzEkZzAkdDE3NDkxNzk3MTgkajU4JGwwJGgw)
[免費影片or圖片練習](https://www.pexels.com/zh-tw/)

### 5. 版面區塊

- `<div> 頁面的區塊、範圍`
  - 預設垂直排列
  - 可在 `style` 屬性內給 `display:inline-block` 水平排列
- `<section> 頁面中的區塊範圍`

**可在div、section中加入style，由垂直排列改成水平排列方式：**

- **`float:`**
  - left
  - right
- **`display:`**
  - block >> 占一整行
  - inline >> 不換行
  - flex >> 彈性排列
  - grid >> 網格系統
- **`position:`**
  - static >> 預設
  - relative >> 以原位置為基準
  - absolute >> 相對最近有定位的父元素
  - fixed >> 固定在畫面上
- **`flex`**
- **`grid`**

### 6. 其他

- `<hr> 呈現水平線`
- `<br> 呈現換行，同個段落內`
- `<span> 呈現文字行中的子項目`
- `<iframe> 呈現頁面中的內置框架，可以連結其他頁面`

---

- 區塊型態
  - 議定有開始飆前也有結束標籤
  - 預設呈現可以表達出寬度與高度的變化
  - 排列方向是由上而下的垂直方向

- 非區塊型態
  - 有開始標籤不一定也有結束標籤
  - 無法表達出寬度與高度的變化
  - 排列方向由下而上的垂直方向

---

## HTML5語意標籤

![20250606150837](https://raw.githubusercontent.com/richard153r/pic/main/pic/20250606150837.png)

- `<header> 頁首、區塊開頭`
  - 加入CSS `<link rel="stylesheet" href="css檔案位置">` &#8251; 必須在header內
- `<nav> 導覽`
- `<aside> 側邊攔`
- `<section> 有標題的內容區塊`
- `<article> 旁邊補充內容`
- `<footer> 頁尾`

---

## HTML 符號

&copy; >> `&copy;`
&#8251; >> `&#8251;`
