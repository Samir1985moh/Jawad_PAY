# -*- coding: utf-8 -*-
from flask import Flask, render_template_string, redirect

app = Flask(__name__)

# ضع هنا رابط الدفع الجاهز الذي حصلت عليه من بوابة الدفع (مثل Stripe أو Tap)
PAYMENT_LINK = "https://your-gateway.com"

@app.route('/')
def home():
    # تصميم صفحة الهبوط للمنتج بشكل سريع وجذاب
    html_content = """
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>شراء نظام ERP الجواد</title>
        <style>
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f7f6; text-align: center; padding: 50px; color: #333; }
            .card { background: white; padding: 40px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); max-width: 50px; margin: 0 auto; max-width: 500px; }
            h1 { color: #2c3e50; }
            p { font-size: 18px; color: #7f8c8d; line-height: 1.6; }
            .price { font-size: 24px; font-weight: bold; color: #27ae60; margin: 20px 0; }
            .btn-pay { background-color: #007bff; color: white; border: none; padding: 15px 35px; font-size: 18px; border-radius: 8px; cursor: pointer; text-decoration: none; display: inline-block; transition: background 0.3s; }
            .btn-pay:hover { background-color: #0056b3; }
            .footer-notes { margin-top: 20px; font-size: 12px; color: #b2bec3; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>نظام ERP لإدارة الشركات</h1>
            <p>حل ذكي ومتكامل لإدارة المبيعات، المخازن، والمحاسبة متوافق مع متطلبات السوق.</p>
            <div class="price">السعر: 500 ريال سعودي</div>
            
            <!-- زر الدفع الذي ينقل العميل لبوابة الدفع المصرفية -->
            <a href="/checkout" class="btn-pay">اشتر الآن (يدعم مدى / Apple Pay)</a>
            
            <div class="footer-notes">الدفع آمن ومصادق عليه من الشبكات المصرفية السعودية</div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_content)

@app.route('/checkout')
def checkout():
    # توجيه العميل مباشرة إلى صفحة الدفع الآمنة
    return redirect(PAYMENT_LINK)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

