from django.shortcuts import render
from django.http import Http404



# 模擬書籍資料（全域變數，方便各 function 使用）
MOCK_BOOKS = [
    {
        'id': 1, 'title': 'Python程式設計', 'author': '王小明',
        'author_slug': 'wang-xiaoming', 'category': 'programming',
        'price': 450, 'isbn': '978-1-234-56789-0', 'year': 2023
    },
    {
        'id': 2, 'title': 'Django網頁開發', 'author': '李小華',
        'author_slug': 'li-xiaohua', 'category': 'web-development',
        'price': 520, 'isbn': '978-1-234-56789-1', 'year': 2024
    },
    {
        'id': 3, 'title': '資料結構與演算法', 'author': '張大同',
        'author_slug': 'zhang-datong', 'category': 'computer-science',
        'price': 380, 'isbn': '978-1-234-56789-2', 'year': 2023
    },
    {
        'id': 4, 'title': '機器學習實戰', 'author': '王小明',
        'author_slug': 'wang-xiaoming', 'category': 'machine-learning',
        'price': 600, 'isbn': '978-1-234-56789-3', 'year': 2024
    },
]

def index(request):
    return render(request, "index.html")

def book_list(request):
    context = {
        'books': MOCK_BOOKS,
        'page_title': '書籍列表'
    }
    return render(request, 'book_list.html', context)

def book_detail(request, book_id):
    try:
        book = next(book for book in MOCK_BOOKS if book['id'] == book_id)
    except StopIteration:
        raise Http404(f"書籍 ID:{book_id} 不存在")

    context = {
        'book': book,
        'page_title': book['title']
    }
    return render(request, 'book_detail.html', context)

def books_by_category(request, category_name):
    books = [book for book in MOCK_BOOKS if book['category'] == category_name]
    if not books:
        raise Http404(f"分類代號: {category_name} 不存在")
    
    context = {
        'books': books,
        'category_name': category_name,
        'page_title': f'{category_name} 的書籍',
    }
    return render(request, 'category.html', context)

def books_by_author(request, author_slug):
    # 過濾出指定作者的書籍
    books = [book for book in MOCK_BOOKS if book['author_slug'] == author_slug]
    if not books:
        raise Http404(f"作者代號: {author_slug} 不存在")
    
    author_name = books[0]['author']

    context = {
        'books': books,
        'author_name': author_name,
        'page_title': f'{author_name} 的書籍',
    }
    return render(request, 'author.html', context)
