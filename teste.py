from datetime import date,timedelta
hoje = date.today() - timedelta(1)

print(hoje.strftime("%d/%m/%Y"))
