# CÓDIGO PARA SIMULAÇÃO DE BURACOS NEGROS POR MEIO DE CÁLCULOS FÍSICO-MATEMÁTICOS
from Neuraline.ComputationalPhysics.black_hole_simulation import BlackHoleSimulation # importa o algoritmo de Simulação de Buracos Negros do módulo de Física Computacional
BLACK_HOLE_BLACK_BODY_ACCRETION_LEVEL = 1.0 # nível de acreção do corpo negro em graus percentuais de 0 (0%) a 1 (100%).
BLACK_HOLE_SPACE_TEMPERATURE_LEVEL = 0.0 # nível da temperatura espacial em relação ao buraco negro de 0 (0%) a 1 (100%).
BLACK_HOLE_BLACK_BODY_EXTERNAL_TEMPERATURE = 60.0 # temperatura externa do corpo negro em nanokelvins.
VISIBLE_LIGHT_SPECTRUM = 370.0 # espectro da luz visível emitida pela acreção de matéria em nanômetros.
BLACK_HOLE_ACCRETION_RADIUS = 1.5 # medida do raio de acreção em radianos.
BLACK_HOLE_ACCRETION_WIDTH = 10.0 # largura de expansão da acreção do buraco negro em dias-luz.
BLACK_HOLE_ACCRETION_GLOW_LEVEL = 0.9 # nível do brilho total causado pela acreção em graus percentuais de 0 (0%) a 1 (100%).
BLACK_HOLE_ACCRETION_TEMPERATURE = 1000000.0 # temperatura de acreção do buraco negro em kelvins.
STARS_GLOW_LEVEL = 1.0 # nível do brilho das estrelas no campo de visão em graus percentuais de 0 (0%) a 1 (100%).
GALAXY_GLOW_LEVEL = 0.4 # nível do brilho da galáxia no campo de visão em graus percentuais de 0 (0%) a 1 (100%).
LEVEL_OF_PLANETARY_ENVIRONMENTAL_IMPACT = 0.1 # nível de brilho do orbital (lua/planeta) causado pelo impacto ambiental no campo de visão em percentuais de 0 (0%) a 1 (100%).
PLANETARY_LUMINOSITY_LEVEL = 1.5 # nível de luminosidade orbital/planetária em graus percentuais de 0 (0%) a 1 (100%).
BLACK_HOLE_N_STEPS = 100 # número de quadros de uma simulação matemática para outra.
BLACK_HOLE_QUALITY = 'medium' # qualidade da simulação, poderá ser medium (qualidade média com processamento médio), fast (qualidade baixa com processamento rápido), high (qualidade alta com processamento lento e alta demanda por hardware).
BLACK_HOLE_ACCRETION_DISK = True # se True, exibirá o disco de acreção, se False, colocará o disco de acreção fora do espectro da luz visível.
PLANET_ENABLED = False # se True, exibirá um orbital (planeta genérico) orbitando o buraco negro, se False, não exibirá o orbital/planeta.
PLANET_DISTANCE = 7.0 # distância do orbital/planeta em relação ao buraco negro em dias-luz.
PLANET_RADIUS = 0.4 # medida do orbital/planeta em radianos.
BLACK_HOLE_LORENTZ_CONTRACTION = True # se True, usará o cálculo da contração de Lorentz-FitzGerald, se False, irá ignorar a contração de Lorentz-FitzGerald.
BLACK_HOLE_GRAVITATIONAL_TIME_DILATION = True # se True, usará o cálculo da dilatação gravitacional do tempo, se False, irá ignorar o cálculo da dilatação do tempo.
BLACK_HOLE_ABERRATION = True # se True, habilitará o fenômeno de aberração, se False, irá ignorar o cálculo de aberração.
BLACK_HOLE_BEAMATION = True # se True, permitirá a transmissão de informação e energia, se False, irá ignorar o cálculo de transmissão.
BLACK_HOLE_DOPPLER_SHIFT = True # se True, usará o cálculo do efeito de deslocamento Doppler, se False, irá ignorar o deslocamento Doppler.
BLACK_HOLE_LIGHT_TRAVEL_TIME = True # se True, usará o cálculo do deslocamento da luz, se False, irá ignorar o cálculo do deslocamento da luz.
BLACK_HOLE_TIME_SCALE = 1.0 # escala temporal do horizonte de eventos em relação ao observador em graus percentuais de 0 (0%) a 1 (100%).
OBSERVER_MOTION = True # se True, habilitará o movimento do observador, se False, irá ignorar o movimento do observador.
OBSERVER_DISTANCE = 11.0 # distância do observador em relação ao disco de acreção na escala de dias-luz.
OBSERVER_ORBITAL_INCLINATION = -10.0 # grau de inclinação orbital do observador.
black_hole = BlackHoleSimulation( # executa a simulação do Buraco Negro através dos cálculos de Astrofísica habilitados ou desabilitados acima.
	BLACK_HOLE_BLACK_BODY_ACCRETION_LEVEL=BLACK_HOLE_BLACK_BODY_ACCRETION_LEVEL, # atribuição do nível de acreção do corpo negro.
	BLACK_HOLE_SPACE_TEMPERATURE_LEVEL=BLACK_HOLE_SPACE_TEMPERATURE_LEVEL, # atribuição do nível de temperatura espacial.
	BLACK_HOLE_BLACK_BODY_EXTERNAL_TEMPERATURE=BLACK_HOLE_BLACK_BODY_EXTERNAL_TEMPERATURE, # atribuição da temperatura externa em nanokelvins.
	VISIBLE_LIGHT_SPECTRUM=VISIBLE_LIGHT_SPECTRUM, # atribuição do espectro de luz visível em nanômetros.
	BLACK_HOLE_ACCRETION_RADIUS=BLACK_HOLE_ACCRETION_RADIUS, # atribuição dos radianos da acreção.
	BLACK_HOLE_ACCRETION_WIDTH=BLACK_HOLE_ACCRETION_WIDTH, # atribuição da largura de expansão da acreção em dias-luz.
	BLACK_HOLE_ACCRETION_GLOW_LEVEL=BLACK_HOLE_ACCRETION_GLOW_LEVEL, # atribuição do nível do brilho de acreção.
	BLACK_HOLE_ACCRETION_TEMPERATURE=BLACK_HOLE_ACCRETION_TEMPERATURE, # atribuição da temperatura causada pela acreção em kelvins.
	STARS_GLOW_LEVEL=STARS_GLOW_LEVEL, # atribuição do nível de brilho das estrelas.
	GALAXY_GLOW_LEVEL=GALAXY_GLOW_LEVEL, # atribuição do nível de brilho da galáxia.
	LEVEL_OF_PLANETARY_ENVIRONMENTAL_IMPACT=LEVEL_OF_PLANETARY_ENVIRONMENTAL_IMPACT, # atribuição do impacto ambiental no corpo orbital.
	PLANETARY_LUMINOSITY_LEVEL=PLANETARY_LUMINOSITY_LEVEL, # atribuição do nível de luminosidade do corpo orbital.
	BLACK_HOLE_N_STEPS=BLACK_HOLE_N_STEPS, # atribuição do número referente a quantidade de quadros por simulação computacional.
	BLACK_HOLE_QUALITY=BLACK_HOLE_QUALITY, # atribuição da qualidade da simulação computacional.
	BLACK_HOLE_ACCRETION_DISK=BLACK_HOLE_ACCRETION_DISK, # atribuição do estado do disco de acreção.
	PLANET_ENABLED=PLANET_ENABLED, # atribuição do estado do corpo orbital.
	PLANET_DISTANCE=PLANET_DISTANCE, # atribuição da distância do corpo orbital em dias-luz.
	PLANET_RADIUS=PLANET_RADIUS, # atribuição da medida do corpo orbital
	BLACK_HOLE_LORENTZ_CONTRACTION=BLACK_HOLE_LORENTZ_CONTRACTION, # atribuição do estado da contração de Lorentz-FitzGerald.
	BLACK_HOLE_GRAVITATIONAL_TIME_DILATION=BLACK_HOLE_GRAVITATIONAL_TIME_DILATION, # atribuição do estado de dilatação gravitacional do tempo.
	BLACK_HOLE_ABERRATION=BLACK_HOLE_ABERRATION, # atribuição do estado da aberração.
	BLACK_HOLE_BEAMATION=BLACK_HOLE_BEAMATION, # atribuição do estado de transmissão de informação e energia representado por iluminação.
	BLACK_HOLE_DOPPLER_SHIFT=BLACK_HOLE_DOPPLER_SHIFT, # atribuição do estado de deslocamento Doppler.
	BLACK_HOLE_LIGHT_TRAVEL_TIME=BLACK_HOLE_LIGHT_TRAVEL_TIME, # atribuição do estado de viagem da luz no tempo.
	BLACK_HOLE_TIME_SCALE=BLACK_HOLE_TIME_SCALE, # atribuição do nível de escala temporal distorcida pelo poço gravitacional.
	OBSERVER_MOTION=OBSERVER_MOTION, # atribuição do estado de movimentação do observador.
	OBSERVER_DISTANCE=OBSERVER_DISTANCE, # atribuição da distância do observador em dias-luz.
	OBSERVER_ORBITAL_INCLINATION=OBSERVER_ORBITAL_INCLINATION # atribuição do grau de inclinação do observador.
) # parâmetros de inicialização da simulação computacional.
ARTIFICIAL_NEURAL_NETWORK, QUANTUM_SIMULATION = False, True # habilitação dos recursos matemáticos aplicados a simulação
black_hole_result = black_hole.run( # execução da simulação computacional utilizando os cálculos dos parâmetros de inicialização.
	ARTIFICIAL_NEURAL_NETWORK=ARTIFICIAL_NEURAL_NETWORK, # atribuição do estado de utilização de redes neurais artificiais na simulação.
	QUANTUM_SIMULATION=QUANTUM_SIMULATION # atribuição do estado de utilização de cálculos de otimização quântica na simulação.
)# parâmetros de execução da simulação computacional.
# estado da simulação, se True a simulação terá sido construída com sucesso, caso contrário poderão existir erros de configuração.
if black_hole_result: print('Simulação de buraco negro executada com sucesso.') # exibição da mensagem de sucesso na operação
else: print('Erro na execução da simulação de buraco negro.') # exibição da mensagem de fracasso na operação