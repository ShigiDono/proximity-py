config = [
	[
		{
			"bottom" : ["Time", "s"],
			"left" : ["Proximity1", "1/ADC"],
			"curves" : [
				{
					"color" : (255, 0, 0),
					"data_size" : 1000
				},
			]
		},
		{
			"bottom" : ["Time", "s"],
			"left" : ["Proximity2", "ADC"],
			"curves" : [
				{
					"color" : (0, 255, 0),
					"data_size" : 1000
				},
			]
		},
		{
			"bottom" : ["Time", "s"],
			"left" : ["Proximity3", "1/ADC"],
			"curves" : [
				{
					"color" : (0, 0, 255),
					"data_size" : 1000
				},
			]
		},
	],
	[
		{
			"bottom" : ["Time", "s"],
			"left" : ["IR Light", "ADC"],
			"curves" : [
				{
					"color" : (128, 0, 0),
					"data_size" : 1000
				},
			]
		},
		{
			"bottom" : ["Time", "s"],
			"left" : ["Visible light", "ADC"],
			"curves" : [
				{
					"color" : (128, 128, 255),
					"data_size" : 1000
				},
			]
		},
		{
			"bottom" : ["Time", "s"],
			"left" : ["UV Index", "UV"],
			"curves" : [
				{
					"color" : (150, 100, 255),
					"data_size" : 1000
				},
			]
		},
	],
]
