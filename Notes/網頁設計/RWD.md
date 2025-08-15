# Bootstrap應用

## test1.html

```html
<!-- <link>標籤 在 HTML 中用來引入外部資源；<script>用來在網頁中載入 JavaScript 程式碼 -->
<link rel="stylesheet" type="text/css" href="bootstrap-5.3.7-dist/css/bootstrap.min.css">
<!--網頁的按鈕、表單、表格、排版等都會自動擁有 Bootstrap 預設的美化與響應式布局功能，不需要你手動寫所有的 CSS -->
<script type="bootstrap-5.3.7-dist/js/bootstrap.min.js"></script>
 <!-- 啟用 Bootstrap 提供的 JavaScript 元件 -->
```

```html
<div class="container">
<!-- class="container" 整個版面的外框；讓內容不會緊貼螢幕邊緣，保有間距 -->
    <div class="row"> <!-- row 水平排版的列 -->
        <div class="col">testing!</div> <!-- col 垂直的欄(放內容用，一列最多12欄) -->
    </div>
</div>
<div class="container-fluid">
<!-- 滿版容器(全螢幕寬度)，不會有固定邊界，適合需要貼滿螢幕的區塊 -->
    <div class="row">
        <div class="col">Lorem ipsum dolor sit amet consectetur, adipisicing elit. Quibusdam soluta voluptatem odio commodi consequatur provident, at, magnam nobis ducimus beatae. Pariatur ipsam impedit vitae maiores temporibus repellendus accusamus qui nulla.</div>
    </div>
```

---

## 建立一個文件範本

1. 先將需要的內文key好
2. 再到 **工具 > 外掛程式開發 > 新增程式碼片段**
![20250810125321](https://raw.githubusercontent.com/richard153r/pic/main/pic/20250810125321.png)
3. 將第3行內文貼上所需的範本&第7行註解關掉 並且自行修改名稱
![20250810131008](https://raw.githubusercontent.com/richard153r/pic/main/pic/20250810131008.png)
4. 記得儲存 **檔案 > 儲存** 可建立一個資料夾，存放裡面 未來可以將資料夾直接提取
![20250810133137](https://raw.githubusercontent.com/richard153r/pic/main/pic/20250810133137.png)
5. 如有需要修改 **設定 > 瀏覽資源包** 到User資料夾內找
![20250810155817](https://raw.githubusercontent.com/richard153r/pic/main/pic/20250810155817.png)

---