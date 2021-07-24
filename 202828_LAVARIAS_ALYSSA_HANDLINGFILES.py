products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}
def get_product(code):
    return products[code]
def get_property(code, property):
    return products[code][property]
def main():
    
    session = ''
    receipt = ''''''
    total = 0
    summary_dict = {}
    
    with open('receipt.txt', 'w') as summary:
        summary.write('''==
CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL\n''')
    
    while True:
        
        session = input('{product_code},{quantity}')
        
        if session != '/':  
            split_input = session.split(',')
            code = split_input[0]
            quantity = int(split_input[1])
            
            if code not in summary_dict:
                summary_dict[code] = quantity
                
            else:
                summary_dict[code] += quantity 
         
        elif session == '/':
            break
    
    for element in sorted(summary_dict):
            name = get_property(element,'name')
            subtotal = get_property(element,'price')*summary_dict[element]
            
            with open('receipt.txt', 'a+') as summary:
                summary.write(f'''{element}\t\t{name}\t\t{summary_dict[element]}\t\t\t\t\t{subtotal}\n''')
            
            total += subtotal
    
    with open('receipt.txt','a+') as summary:       
        summary.write(f'''\nTotal:\t\t\t\t\t\t\t\t\t\t\t\t{total}
==''')
main()
