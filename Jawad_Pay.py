# -*- coding: utf-8 -*-
from flask import Flask, render_template_string, redirect

app = Flask(__name__)

# رابط الدفع التجريبي (ستستبدله لاحقاً برابط الفاتورة أو المنتج من Paddle)
PAYMENT_LINK = "https://your-gateway.com"

@app.route('/')
def home():
    html_content = """
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>نظام جواد ERP المتكامل</title>
        <style>
            body { font-family: system-ui, -apple-system, sans-serif; background-color: #f8fafc; margin: 0; padding: 0; color: #1e293b; text-align: center; }
            .navbar { background: #ffffff; padding: 15px; box-shadow: 0 1px 3px rgba(0,0,0,0.05); font-weight: bold; font-size: 20px; color: #0f172a; }
            .container { max-width: 900px; margin: 40px auto; padding: 20px; }
            .hero-card { background: white; padding: 40px; border-radius: 16px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); margin-bottom: 30px; }
            h1 { color: #0f172a; margin-bottom: 10px; }
            .tagline { font-size: 18px; color: #64748b; line-height: 1.6; margin-bottom: 25px; }
            
            /* قسم معرض الصور */
            .gallery-title { font-size: 22px; font-weight: bold; margin: 40px 0 20px 0; color: #0f172a; }
            .gallery-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 20px; margin-bottom: 40px; }
            .photo-card { background: white; padding: 10px; border-radius: 12px; box-shadow: 0 2px 4px rgba(0,0,0,0.02); border: 1px solid #e2e8f0; }
            .photo-card img { width: 100%; border-radius: 8px; height: 180px; object-fit: cover; background: #e2e8f0; }
            .photo-caption { font-size: 14px; color: #475569; margin-top: 8px; font-weight: 500; }
            
            .price { font-size: 28px; font-weight: 800; color: #10b981; margin: 25px 0; }
            .btn-pay { background-color: #2563eb; color: white; border: none; padding: 16px 40px; font-size: 18px; border-radius: 12px; cursor: pointer; text-decoration: none; display: inline-block; font-weight: bold; transition: background 0.2s; box-shadow: 0 4px 6px -1px rgba(37,99,235,0.2); }
            .btn-pay:hover { background-color: #1d4ed8; }
            
            .links { margin-top: 50px; padding: 20px 0; border-top: 1px solid #e2e8f0; }
            .links a { color: #2563eb; text-decoration: none; margin: 0 12px; font-size: 14px; }
        </style>
    </head>
    <body>
        <div class="navbar">الجواد لتقنية المعلومات</div>
        
        <div class="container">
            <div class="hero-card">
                <h1>نظام ERP المتكامل لإدارة الشركات</h1>
                <p class="tagline">حل ذكي شامل لإدارة الحسابات، المخازن، المبيعات، والمشتريات مصمم خصيصاً لتلبية احتياجات نمو أعمالك ومطابق للمواصفات السحابية.</p>
                
                <a href="/checkout" class="btn-pay">الانتقال الآمن للسداد (مدى / Apple Pay)</a>
            </div>

            <!-- بداية قسم استعراض صور النظام -->
            <div class="gallery-title">📱 جولة داخل واجهات النظام</div>
            <div class="gallery-grid">
                <!-- الصورة الأولى: لوحة التحكم -->
                <div class="photo-card">
                    <img src="https://githubusercontent.com/Samir1985moh/Jawad_PAY/main/Control%20Panel.png" alt="لوحة التحكم الرئيسية">
                    <div class="photo-caption">لوحة التحكم والمؤشرات الإحصائية العامة</div>
                </div>
                
                <!-- الصورة الثانية: إدارة المخازن -->
                <div class="photo-card">
                    <img src="https://githubusercontent.com/Samir1985moh/Jawad_PAY/main/Reports.png" alt="إدارة المخازن">
                    <div class="photo-caption">شاشة جرد المخازن وإدارة المنتجات</div>
                </div>
                
                <!-- الصورة الثالثة: المبيعات والفواتير -->
                <div class="photo-card">
                    <img src="Sales.png" alt="المبيعات والفواتير">
                    <div class="photo-caption">إصدار الفواتير وإدارة مبيعات العملاء</div>
                </div>
            </div>
            <!-- نهاية قسم استعراض صور النظام -->

            <div class="links">
                <a href="/pricing">صفحة الأسعار</a> | 
                <a href="/terms">الشروط والأحكام</a> | 
                <a href="/privacy">سياسة الخصوصية</a>
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_content)

@app.route('/pricing')
def pricing():
    html_content = """
    <body style="font-family:sans-serif; text-align:center; padding:50px; background:#f8fafc; color:#1e293b;">
        <div style="background:white; padding:40px; border-radius:16px; max-width:500px; margin:0 auto; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
            <h2>تفاصيل أسعار نظام ERP</h2>
            <p>يتم تحديد القيمة بناءً على حجم النظام والاتفاق المباشر بالفاتورة اليدوية، ويشمل الدعم الفني والصيانة.</p>
            <br>
            <a href="/" style="color:#2563eb; text-decoration:none; font-weight:bold;">العودة للرئيسية</a>
        </div>
    </body>
    """
    return render_template_string(html_content)

@app.route('/terms')
def terms():
    return "<div style='text-align:center; padding:50px; font-family:sans-serif;'><h2>الشروط والأحكام</h2><p>باستخدامك لهذا النظام، فإنك توافق على شروط الاستخدام وحماية الملكية الفكرية الخاصة بالمطور جواد.</p><a href='/'>العودة</a></div>"

@app.route('/privacy')
def privacy():
    return "<div style='text-align:center; padding:50px; font-family:sans-serif;'><h2>سياسة الخصوصية</h2><p>نحن نحترم خصوصية بياناتكم تماماً. النظام يعمل ببيئة آمنة ولا نقوم بمشاركة أي بيانات حساسة تخص عملائكم.</p><a href='/'>العودة</a></div>"

@app.route('/checkout')
def checkout():
    return redirect(PAYMENT_LINK)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
