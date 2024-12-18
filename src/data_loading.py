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
                    yaxis_title="Price", width=1080, height=760,
                    xaxis_rangeslider_visible=False)
    
    # Display the chart
    return fig

if __name__ == '__main__':
    visualize_data(symbol='AAPL', start_date='2024-12-01', end_date='2024-12-31', interval='1d')