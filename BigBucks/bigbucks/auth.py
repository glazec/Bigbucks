from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

import os
from supabase import create_client, Client
url="https://lhjpufbcymwhprgzfbwt.supabase.co"
key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImxoanB1ZmJjeW13aHByZ3pmYnd0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2Nzk2MDY3MDMsImV4cCI6MTk5NTE4MjcwM30.42A0qtrLYChbrdUzjf1E7TRgHionW5xrZRK-e9wBqPk"

supabase = create_client(url, key)

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register',methods=('GET','POST'))
def register():
    if request.method == 'POST':
        firstname = request.form['InputFirstName']
        lastname = request.form['InputLastName']
        phonenum = request.form['InputPhoneNumber']
        email = request.form['InputEmail']
        username = request.form['InputUserName']
        password = request.form['InputPassword']
        error = None
        if not email:
            error = 'Email is required.'
        elif not firstname:
            error = 'Firstname is required.'
        elif not lastname:
            error = 'Lastname is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            # Unique requirement for Username
            response = supabase.table('Customer_Information').select("*").eq('user_name',username).execute()
            # print(response)
            if response.data:
                error = f"Username {username} is already registered."
            else:
                # Register data into database
                supabase.table('Customer_Information').\
                insert({'first_name': firstname, 'last_name': lastname, 'phone_number': phonenum, 'email_address': email,'user_name': username}).execute()
                supabase.table('Customer_Password').\
                insert({'password':password}).execute()
                return redirect(url_for('auth.login'))
        flash(error)
    return render_template('auth/register.html')

@bp.route('/login',methods=('GET','POST'))
def login():
    if request.method == 'POST':
        username = request.form['InputUsername']
        password = request.form['InputPassword']
        error = None
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        else:
            # Check if Username and password match
            response = supabase.table('Customer_Information').select("*").eq('user_name',username).execute()
            if response.data:
                customer_id = response.data[0]['customer_id']
                # print(customer_id)
                response = supabase.table('Customer_Password').select("password").eq('customer_id',customer_id).execute()
                password_true = response.data[0]['password']
                # print(password_true)
                if password_true == password:
                        session.clear()
                        session['customer_id'] = customer_id
                        return redirect(url_for('index'))
            error = 'Incorrect email or password.'
        flash(error)
    return render_template('auth/login.html')
