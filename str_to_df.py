#!/usr/bin/env python

# import pandas library
import pandas as pd


# Output display options using
desired_width = 320
column_number = 10
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', column_number)


# various fields and values in string format
rank = "1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25	26	27	28	29	30	31	32	33	34	35	36	37	38	39	40" \
       "	41	42	43	44	45	46	47	48	49	50	51	52	53	54	55	56	57	58	59	60	61	62	63	64	65	66	67	68	69	70	71	72" \
       "	73	74	75	76	77	78	79	80	81	82	83	84	85	86	87	88	89	90	91	92	93	94	95	96	97	98	99	100	101	102	103	104	105" \
       "	106	107	108	109	110	111	112	113	114	115	116	117	118	119	120	121	122	123	124	125	126	127	128	129	130	131	132" \
       "	133	134	135	136	137	138	139	140	141	142	143	144	145	146	147	148	149	150	151	152	153	154" \
       "	155	156	157	158	159	160	161	162	163	164	165	166	167	168	169	170	171	172	173" \
       "	174	175	176	177	178	179	180	181	182	183	184	185	186	187	188	189	190	191	192" \
       "	193	194	195	196	197	198	199	200	201"


country = "Martinique	Curaçao	Latvia	Lithuania	Ukraine" \
          "	China, Hong Kong SAR	Guadeloupe	Russian Federation" \
          "	Belarus	Estonia	Armenia	El Salvador	Portugal	Hungary	Aruba" \
          "	United States Virgin Islands	Georgia	Barbados" \
          "	China, Macao SAR	Antigua and Barbuda	Republic of Moldova	Puerto Rico	Sri Lanka	Croatia	Uruguay	Poland" \
          "	Kazakhstan	Réunion	Swaziland	Romania	Lesotho	Nepal	Namibia	Slovakia	Bulgaria" \
          "	Zimbabwe	Italy	Mozambique	Cambodia	Thailand	Myanmar	Japan	Serbia" \
          "	Dem. People's Republic of Korea	Argentina	Bahamas	Austria	Saint Lucia	Angola	Rwanda" \
          "	Spain	Bosnia and Herzegovina	Senegal	South Africa	Mayotte	Czechia	France	Belgium" \
          "	Guinea-Bissau	New Zealand	Burundi	Brazil	Germany	Turkey	Guatemala	Finland	Colombia" \
          "	Turkmenistan	Greece	United Kingdom	Nicaragua	Kiribati	Montenegro	Central African Republic" \
          "	Trinidad and Tobago	Singapore	Tunisia	Botswana	United Republic of Tanzania	Haiti	Viet Nam" \
          "	United States of America	Morocco	Switzerland	Sierra Leone	Gambia	Mongolia	Malawi	Chile" \
          "	Mauritius	Seychelles	Kyrgyzstan	Channel Islands	Israel	Ireland	Canada	Slovenia	Zambia	Kenya" \
          "	Netherlands	Uganda	Denmark	Ghana	Jamaica	Azerbaijan	Mexico" \
          "	Venezuela (Bolivarian Republic of)	Sao Tome and Principe	Cabo Verde	Burkina Faso" \
          "	Somalia	Uzbekistan	Dominican Republic	Togo	Benin	Australia" \
          "	Lao People's Democratic Republic	Belize	Honduras	Madagascar" \
          "	Democratic Republic of the Congo	Ethiopia	Sudan	Peru	Sweden" \
          "	French Guiana	Ecuador	TFYR Macedonia	Mali	China, Taiwan Province of China	Congo" \
          "	Cameroon	Costa Rica	Cuba	Chad	Republic of Korea	South Sudan	Cyprus" \
          "	Bolivia (Plurinational State of)	Eritrea	Niger	Guinea	Tonga	Panama	Grenada	Malta	Iceland" \
          "	Luxembourg	Djibouti	Suriname	Lebanon	Tajikistan	Iran (Islamic Republic of)	Norway	Mauritania" \
          "	Guyana	Indonesia	Philippines	Liberia	Comoros	Saint Vincent and the Grenadines	Bangladesh" \
          "	New Caledonia	Albania	Libya	Algeria	Yemen	Egypt	Syrian Arab Republic	Iraq" \
          "	Vanuatu	Nigeria	Jordan	Guam	State of Palestine	Paraguay	Côte d'Ivoire" \
          "	Timor-Leste	Solomon Islands	Fiji	Papua New Guinea" \
          "	French Polynesia	Micronesia (Fed. States of)	Pakistan	Gabon" \
          "	Brunei Darussalam	China	Afghanistan	Samoa	Malaysia	India" \
          "	Western Sahara	Bhutan	Equatorial Guinea	Maldives	Saudi Arabia" \
          "	Kuwait	Bahrain	Oman	United Arab Emirates	Qatar"


sex_ratio = "83.919	84.34	84.831	85.359	85.913	85.947	86.603	86.769	87	87.866	88.654	88.855" \
            "	90.031	90.586	90.605	91.224	91.303	91.987	92.186	92.233	92.466	92.541	92.954" \
            "	92.986	93.31	93.44	93.888	93.896	94.007	94.043	94.178	94.242	94.539	94.564" \
            "	94.652	94.799	94.824	95.192	95.213	95.427	95.459	95.534	95.587	95.705	95.818" \
            "	95.88	95.906	96.036	96.113	96.169	96.355	96.392	96.393	96.473	96.513	96.608" \
            "	96.609	96.678	96.683	96.734	96.745	96.757	96.787	96.818	96.822	96.901	96.971" \
            "	96.986	96.999	97.184	97.209	97.212	97.325	97.328	97.399	97.592	97.669	97.681" \
            "	97.702	97.853	97.88	97.902	97.938	97.963	97.979	98.03	98.071	98.091	98.108" \
            "	98.133	98.257	98.332	98.335	98.391	98.402	98.426	98.457	98.473	98.812	98.853" \
            "	98.907	98.914	99.026	99.041	99.059	99.152	99.152	99.163	99.186	99.196	99.283" \
            "	99.3	99.315	99.318	99.327	99.361	99.378	99.401	99.412	99.42	99.465	99.698" \
            "	99.805	99.806	99.927	99.952	99.972	99.972	100.039	100.067	100.09	100.119	100.135" \
            "	100.156	100.185	100.22	100.304	100.311	100.312	100.356	100.387	100.451	100.562	100.565" \
            "	100.644	100.649	100.693	100.755	100.803	100.863	100.93	101.083	101.327	101.391	101.447" \
            "	101.466	101.495	101.504	101.656	101.749	101.842	101.86	101.908	101.961	101.998	102.003" \
            "	102.139	102.242	102.349	102.441	102.609	102.635	102.714	102.739	102.904	103.031	103.063" \
            "	103.18	103.382	103.445	103.542	104.018	104.972	105.638	105.707	106.254	106.274	106.379" \
            "	106.551	106.942	107.625	110.528	113.416	123.043	130.216	130.943	134.999	161.256	184.414" \
            "	272.19	306.565"


female_per_100_male = "119.163	118.568	117.881	117.152	116.397	116.351	115.469	115.249	114.943	113.81	112.798" \
                      "	112.543	111.073	110.392	110.369	109.62	109.525	108.711	108.476	108.421	108.148	108.06" \
                      "	107.58	107.543	107.17	107.021	106.51	106.501	106.375	106.334	106.182	106.11	105.776" \
                      "	105.748	105.65	105.486	105.459	105.051	105.028	104.792	104.757	104.675	104.617	104.488" \
                      "	104.365	104.297	104.269	104.128	104.044	103.984	103.783	103.743	103.742	103.656	103.613" \
                      "	103.511	103.51	103.436	103.431	103.376	103.365	103.352	103.32	103.287	103.282	103.198" \
                      "	103.124	103.108	103.094	102.898	102.871	102.868	102.749	102.745	102.67	102.467	102.387" \
                      "	102.374	102.352	102.194	102.166	102.143	102.105	102.079	102.063	102.01	101.967	101.946" \
                      "	101.928	101.903	101.774	101.696	101.693	101.635	101.624	101.599	101.567	101.551	101.202" \
                      "	101.16	101.105	101.098	100.984	100.968	100.95	100.855	100.855	100.844	100.821	100.811" \
                      "	100.722	100.705	100.69	100.687	100.678	100.643	100.626	100.603	100.591	100.583	100.538" \
                      "	100.303	100.195	100.194	100.073	100.048	100.028	100.028	99.961	99.933	99.91	99.881" \
                      "	99.865	99.844	99.815	99.78	99.697	99.69	99.689	99.645	99.614	99.551	99.441" \
                      "	99.438	99.36	99.355	99.312	99.251	99.203	99.144	99.079	98.929	98.69	98.628" \
                      "	98.574	98.555	98.527	98.518	98.371	98.281	98.191	98.174	98.128	98.077	98.041" \
                      "	98.036	97.906	97.807	97.705	97.617	97.457	97.433	97.358	97.334	97.178	97.058" \
                      "	97.028	96.918	96.729	96.67	96.579	96.137	95.263	94.663	94.601	94.114" \
                      "	94.096	94.004	93.852	93.509	92.915	90.475	88.171	81.272	76.795	76.369" \
                      "	74.075	62.013	54.226	36.739	32.62"


continent = "North America	North America	Europe	Europe	Europe	Asia	North America	Europe	Europe	Europe" \
            "	Asia	North America	Europe	Europe	North America	North America	Asia	North America" \
            "	Asia	North America	Europe	North America	Asia	Europe	South America	Europe	Asia" \
            "	Africa	Africa	Europe	Africa	Asia	Africa	Europe	Europe	Africa	Europe	Africa	Asia" \
            "	Asia	Asia	Asia	Europe	Asia	South America	North America	Europe	North America" \
            "	Africa	Africa	Europe	Europe	Africa	Africa	Africa	Europe	Europe	Europe	Africa	Oceania" \
            "	Africa	South America	Europe	Asia	North America	Europe	South America	Asia	Europe" \
            "	Europe	North America	Oceania	Europe	Africa	North America	Asia	Africa	Africa	Africa" \
            "	North America	Asia	North America	Africa	Europe	Africa	Africa	Asia	Africa" \
            "	South America	Africa	Africa	Asia	Europe	Asia	Europe	North America	Europe	Africa" \
            "	Africa	Europe	Africa	Europe	Africa	North America	Asia	North America	South America" \
            "	Africa	Africa	Africa	Africa	Asia	North America	Africa	Africa	Oceania	Asia" \
            "	North America	North America	Africa	Africa	Africa	Africa	South America	Europe" \
            "	South America	South America	Europe	Africa	Asia	Africa	Africa	North America" \
            "	North America	Africa	Asia	Africa	Asia	South America	Africa	Africa	Africa" \
            "	Oceania	North America	North America	Europe	Europe	Europe	Africa	South America" \
            "	Asia	Asia	Asia	Europe	Africa	South America	Asia	Asia	Africa	Africa" \
            "	North America	Asia	Oceania	Europe	Africa	Africa	Asia	Africa	Asia	Asia" \
            "	Oceania	Africa	Asia	Oceania	Asia	South America	Africa	Asia	Oceania	Oceania" \
            "	Oceania	Oceania	Oceania	Asia	Africa	Asia	Asia	Asia	Oceania	Asia	Asia" \
            "	Africa	Asia	Africa	Asia	Asia	Asia	Asia	Asia	Asia	Asia"


# converting the set of strings to a set of python lists
rank_list = rank.split(sep="\t")
country_list = country.split(sep="\t")
sex_ratio_list = sex_ratio.split(sep="\t")
female_per_100_male_list = female_per_100_male.split(sep="\t")
continent_list = continent.split(sep="\t")


# converting the set of python lists to pandas series
countries_by_sex_ratio_count = {'Rank': pd.Series(rank_list), 'Country/Territory': pd.Series(country_list),
                       'Sex Ratio': pd.Series(sex_ratio_list), 'Female per 100 male': pd.Series(female_per_100_male_list),
                       'Continent': pd.Series(continent_list)}


# converting the set of pandas series to a dataframe
countries_by_sex_ratio_count_df = pd.DataFrame(countries_by_sex_ratio_count)


# printing out the fields in python list format
print("Rank List", "\n", rank_list, "\n")
print("Country List", "\n", country_list, "\n")
print("Sex Ratio List", "\n", sex_ratio_list, "\n")
print("Female per 100 Male List", "\n", female_per_100_male_list, "\n")
print("Continent List", "\n", continent_list, "\n")

# printing out the pandas data frame
print(countries_by_sex_ratio_count_df)