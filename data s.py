from datascience import*
ice=Table().with_columns(
    'Flavour',make_array('strawbery','choclate','choclate','strawbery'),
    'Price',make_array(3.55,4.75,2.33,3.99))
ice.group('Flavour',sum)
