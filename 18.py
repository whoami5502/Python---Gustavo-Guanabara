import math
angulo = float(input('Digite o ângulo que você deseja:  '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f'Seu ângulo é {angulo}, portanto seu seno é {seno:.2f}, seu cosseno é {cosseno:.2f} e seu tangente é {tangente:.2f}')
