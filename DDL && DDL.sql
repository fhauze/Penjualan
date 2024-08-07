-- Create tables
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    category VARCHAR(50) NOT NULL,
    variant VARCHAR(50),
    price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    table_number VARCHAR(10) NOT NULL,
    order_id INT REFERENCES orders(id) ON DELETE CASCADE,
    promotion_id INT REFERENCES promotions(id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE order_items (
    id SERIAL PRIMARY KEY,
    order_id INT REFERENCES orders(id) ON DELETE CASCADE,
    product_id INT REFERENCES products(id) ON DELETE CASCADE,
    quantity INT NOT NULL,
    total_price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE promotions (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    details TEXT NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE order_promotions (
    id SERIAL PRIMARY KEY,
    order_id INT REFERENCES orders(id) ON DELETE CASCADE,
    promotion_id INT REFERENCES promotions(id) ON DELETE CASCADE,
    quantity INT NOT NULL,
    total_price DECIMAL(10, 2) NOT NULL
);

-- Insert initial data into products
INSERT INTO products (name, category, variant, price) VALUES
('Jeruk', 'Minuman', 'DINGIN', 12000),
('Jeruk', 'Minuman', 'PANAS', 10000),
('Teh', 'Minuman', 'MANIS', 8000),
('Teh', 'Minuman', 'TAWAR', 5000),
('Kopi', 'Minuman', 'DINGIN', 8000),
('Kopi', 'Minuman', 'PANAS', 6000),
('Extra Es Batu', 'Minuman', NULL, 2000),
('Mie', 'Makanan', 'GORENG', 15000),
('Mie', 'Makanan', 'KUAH', 15000),
('Nasi Goreng', 'Makanan', NULL, 15000);

-- Insert initial data into promotions
INSERT INTO promotions (name, details, price) VALUES
('Nasi Goreng + Jeruk Dingin', 'Nasi Goreng + Jeruk Dingin', 23000);
