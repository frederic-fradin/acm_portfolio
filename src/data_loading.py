import yfinance as yf
import plotly.graph_objects as go


def visualize_data(symbol:str, start_date:object, end_date:object, interval:str) -> object:
    # Load data
    ticker = yf.Ticker(symbol)
    data = ticker.history(start=start_date, end=end_date, interval=interval)

    # Create candlestick chart
    fig = go.Figure(data=[go.Candlestick(x=data.index,
                                        open=data['Open'],
                                        high=data['High'],
                                        low=data['Low'],
                                        close=data['Close'])])

    # Customize the chart layout
    fig.update_layout(title=f"Ticker {symbol} ({start_date} | {end_date} | {interval})",
                    yaxis_title="Price", width=1080, height=540,
                    xaxis_rangeslider_visible=False)
    
    ticker_news = ticker.news
    articles_dict = {}

    # Iterate through the list of news articles and extract the title and link
    for article in ticker_news:
        title = article['title']
        link = article['link']
        articles_dict[title] = link

    # Initialize an empty string to store the markdown content
    markdown_content = ""

    # Loop through each article in the dictionary to format it as markdown
    for title, link in articles_dict.items():
        markdown_content += f"{title} : [URL]({link})\n\n"

    ticker_target = ticker.analyst_price_targets

    # Display the chart
    return fig, markdown_content, ticker_target, data

if __name__ == '__main__':
    visualize_data(symbol='AAPL', start_date='2024-12-01', end_date='2024-12-31', interval='1d')