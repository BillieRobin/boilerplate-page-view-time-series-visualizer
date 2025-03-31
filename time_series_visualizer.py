import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


# Import data (Make sure to parse dates and set the index to 'date')
df = pd.read_csv("fcc-forum-pageviews.csv")
df["date"] = pd.to_datetime(df["date"])
df.set_index("date", inplace=True)

# Clean data by filtering out top and bottom 2.5% of page views
df = df[(df["value"] >= df["value"].quantile(0.025)) & (df["value"] <= df["value"].quantile(0.975))]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df.index, df['value'], color='r', linewidth=1)
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    
    # Save image and return figure
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Prepare data for bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()
    
    # Group by year and month to calculate the average page views
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()
    
    # Draw bar plot
    fig = df_bar.plot(kind='bar', figsize=(12, 6), legend=True).get_figure()
    plt.title("Average Daily Page Views per Month")
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title="Months", bbox_to_anchor=(1.05, 1), loc='upper left')
    
    # Save image and return figure
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    
    # Fix: Use pandas datetime accessors directly
    df_box['year'] = df_box['date'].dt.year  # No need for .astype(int)
    df_box['month'] = df_box['date'].dt.strftime('%b')
    
    # Rest of the code remains the same
    fig, axes = plt.subplots(1, 2, figsize=(32, 10), dpi=100)
    
    # Yearly boxplot
    sns.boxplot(x="year", y="value", data=df_box, ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")
    
    # Monthly boxplot
    month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
                   "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    sns.boxplot(x="month", y="value", data=df_box, order=month_order, ax=axes[1])
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    fig.savefig('box_plot.png')
    return fig

"""
def draw_box_plot():
    # Prepare data (keep existing code)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date].astype(int)  # Ensure integer type
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df_box['value'] = pd.to_numeric(df_box['value'])  # Ensure numeric type

    # Modify boxplot calls
    fig, axes = plt.subplots(1, 2, figsize=(32, 10), dpi=100)
    
    # Yearly boxplot
    sns.boxplot(x="year", y="value", data=df_box, ax=axes[0])
    
    # Monthly boxplot
    month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
                   "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    sns.boxplot(x="month", y="value", data=df_box, order=month_order, ax=axes[1])


  # Save image and return figure
    fig.savefig('box_plot.png')
    return fig

"""
  







"""
# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = None

# Clean data
df = None


def draw_line_plot():
    # Draw line plot





    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = None

    # Draw bar plot





    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
"""
