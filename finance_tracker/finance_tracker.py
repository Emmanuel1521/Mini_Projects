from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import plotly.graph_objs as go
from plotly.subplots import make_subplots

app = Flask(__name__)

# Dummy data for expenses
expenses = []
expense_id = 1  # Initialize expense ID counter

# Define routes
@app.route('/')
def index():
    return render_template('tracker.html', expenses=expenses)

@app.route('/add_expense', methods=['POST'])
def add_expense():
    global expense_id  # Use global variable for expense ID
    description = request.form['description']
    category = request.form['category']
    amount = float(request.form['amount'])
    date = datetime.strptime(request.form['date'], '%Y-%m-%d')
    # Create a new expense with an auto-incrementing ID
    new_expense = {'id': expense_id, 'description': description, 'category': category, 'amount': amount, 'date': date}
    expenses.append(new_expense)
    expense_id += 1  # Increment expense ID for the next expense
    return redirect(url_for('index'))

@app.route('/visualization')
def visualize():
    categories = {}
    expenses_by_category = []

    # Calculate expenses by category
    for expense in expenses:
        if expense['category'] not in categories:
            categories[expense['category']] = 0
        categories[expense['category']] += expense['amount']

    for category, amount in categories.items():
        expenses_by_category.append((category, amount))

    expenses_by_category.sort(key=lambda x: x[1], reverse=True)

    # Create a bar chart for expenses by category
    bar_chart = go.Bar(x=[x[0] for x in expenses_by_category], y=[x[1] for x in expenses_by_category])

    # Create a line chart for expenses over time
    expenses_over_time = sorted(expenses, key=lambda x: x['date'])
    line_chart = go.Scatter(x=[expense['date'] for expense in expenses_over_time],
                            y=[expense['amount'] for expense in expenses_over_time],
                            mode='lines+markers')

    # Create subplot for both charts
    fig = make_subplots(rows=1, cols=2, subplot_titles=("Expenses by Category", "Expenses Over Time"))
    fig.add_trace(bar_chart, row=1, col=1)
    fig.add_trace(line_chart, row=1, col=2)

    # Update layout
    fig.update_layout(showlegend=False)

    # Convert plotly figure to JSON for rendering in HTML
    plot_div = fig.to_html(full_html=False)

    return render_template('visualization.html', plot_div=plot_div)

if __name__ == '__main__':
    app.run(debug=True)
