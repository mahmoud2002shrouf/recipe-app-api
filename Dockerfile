ARG PYTHON_VERSION=3.12-alpine
FROM python:${PYTHON_VERSION}
LABEL maintainer="shrouf"
ENV PYTHONUNBUFFERED=1

# نسخ ملفات المتطلبات
COPY /requirements.txt /tmp/requirements.txt
COPY /requirements.dev.txt /tmp/requirements.dev.txt

# إعداد الدليل الرئيسي للتطبيق
COPY ./app /app
WORKDIR /app
EXPOSE 8000

# متغير لتحديد البيئة (تطوير أو إنتاج)
ARG DEV=false

# تثبيت الحزم وتنصيب المتطلبات
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client gettext && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
        then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    apk del .tmp-build-deps && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

# إضافة مسار Python الافتراضي إلى PATH
ENV PATH="/py/bin:$PATH"

# تغيير المستخدم إلى django-user
USER django-user