kk = 'total=35.35 user=32.32 nice=0.0 system=3.03 idle=64.65 iowait=0.0 irq=0.0 softirq=0.0 steal=0.0 guest=0.0'

result = {key:float(value) for key,value in map(lambda x:(x.split('=')), kk.split(' '))}
print result