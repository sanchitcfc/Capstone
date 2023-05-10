import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


def viz():
    dataset = pd.read_csv('Friday.csv')

    columns_to_visualize = [
        'Dst Port', 'Protocol', 'Flow Duration', 'Tot Fwd Pkts', 'Tot Bwd Pkts',
        'Fwd Pkt Len Max', 'Bwd Pkt Len Max', 
        'Flow IAT Mean', 'Flow IAT Std', 'Fwd PSH Flags', 'Bwd PSH Flags',
        'Fwd URG Flags', 'Bwd URG Flags', 'SYN Flag Cnt', 'RST Flag Cnt',
        'PSH Flag Cnt', 'ACK Flag Cnt', 'URG Flag Cnt', 'CWE Flag Count',
        'ECE Flag Cnt'
    ]

    for column in columns_to_visualize:
        plt.figure()
        plt.title(f'{column} Distribution')
        dataset[column].plot(kind='hist', rwidth=0.8)
        plt.xlabel(column)
        plt.ylabel('Frequency')
        st.pyplot()  


