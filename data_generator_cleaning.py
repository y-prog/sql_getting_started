import pandas as pd
import numpy as np

# Generate the `orders` dataset (20 rows)
orders_data = {
    'order_id': range(1, 21),  # Order IDs from 1 to 20
    'customer_id': [1001, 1002, 1001, 1003, 1004, 1005, 1006, 1001, 1002, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1004, 1006],
    'product_id': ['A01', 'A02', 'A01', 'A03', 'A02', 'A01', 'A04', None, 'A02', 'A03', 'A05', 'A06', 'A01', 'A07', 'A08', 'A09', 'A05', 'A01', 'A01', 'A03'],
    'quantity': [2, 1, 1, 3, 4, 1, 5, 2, 6, None, 2, 3, 1, 1, 2, 4, 6, 3, 3, 10],  # Include some high values (outliers) and NaNs
    'price_per_item': [10.50, 20.00, 10.50, 15.00, 20.00, 10.50, 25.00, 10.50, 20.00, 15.00, 12.00, None, 10.50, 18.00, 22.00, 30.00, 12.00, 10.50, 1500.00, 9.00],
    'order_date': ['2024-12-01', '2024-12-02', '2024-12-03', '2024-12-05', '2024-12-05', None, '2024-12-07', '2024-12-08', '2024-12-09', '2024-12-10', '2024-12-11', '2024-12-12', '2024-12-13', None, '2024-12-15', '2024-12-16', '2024-12-17', '2024-12-18', '2024-12-19', '2024-12-20'],
}

df = pd.DataFrame(orders_data)
