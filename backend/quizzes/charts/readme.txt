Usage example:

    import charts

    products = charts.get_products()

    # let we have the product_id according to user's choice
    product_id = 100

    # let we have somatype values 
    soma_type = [-2, 10, 26, 5, 1]

    # call the function
    info = charts.get_chart_info(product_id, soma_type, 'Иван', gender=charts.Gender.MALE)

    # or a simpler form
    info = charts.get_chart_info(product_id, soma_type)

    # dumping the response
    print(charts.export_chart_info(info))