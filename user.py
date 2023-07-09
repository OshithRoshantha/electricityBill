import unitPriceCal 
print('--------------------------------------------------------------')
print('               Welcome to CEB Bill Calculator')
print('--------------------------------------------------------------')
print('  Domestic Category                           Connection-30A ')
print('--------------------------------------------------------------')
noUnits=int(input('Please enter the amount of Units(kWh) Consumed: '))
print('--------------------------------------------------------------')

fixed=unitPriceCal.chargeFixed(noUnits)
unitChrg=unitPriceCal.chargeOnUnits(noUnits)

print('Fixed Charge:\t\t\t\t\tRs.'+str(fixed)+'.00')
print('Charge on consumed Units:\t\t\tRs.'+str(unitChrg)+'.00')
print('--------------------------------------------------------------')
print('Amount has to Pay:\t\t\t\tRs.'+str(fixed+unitChrg)+'.00')
print('--------------------------------------------------------------')
