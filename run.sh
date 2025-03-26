#!/bin/bash
echo "======================================"
echo "تشغيل القاموس العربي..."
echo "======================================"
echo "تثبيت المكتبات المطلوبة..."
pip install flask flask-sqlalchemy email-validator gunicorn psycopg2-binary
echo "======================================"
echo "بدء تشغيل التطبيق..."
echo "يمكنك الوصول للتطبيق عبر: http://localhost:5000"
echo "======================================"
python main.py