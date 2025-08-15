import requests
from bs4 import BeautifulSoup
import json
import re

# 1. Coletar dados da primeira URL
url_navios = "http://10.205.144.95/sistram5/servico/busca_naesp.php"
proxies = {"http": "http://10009761:M%40rinha10009761@proxy-3dn.mb:6060","https": "http://10009761:M%40rinha10009761@proxy-3dn.mb:6060",}
res = requests.get(url_navios, proxies=proxies)
embarcacoes = res.json()
# Dados mockados para teste local
# embarcacoes = json.loads("""[
# {"lon":"-173.13631166666667","lat":"53.91133333333333","mmsi":"352002520","nome_navio":"PAVO BREEZE","rumo":"81","id_origem_dados":"29","dh":"2025-06-26 20:54:00","cor":"orange"},
# {"lon":"-153.24483166666667","lat":"47.21811833333334","mmsi":"373721000","nome_navio":"EVER LADEN","rumo":"106","id_origem_dados":"29","dh":"2025-06-26 20:55:55","cor":"yellow"},
# {"lon":"-122.95074","lat":"46.10381833333334","mmsi":"538010605","nome_navio":"ALPHA FLAME","rumo":"118","id_origem_dados":"29","dh":"2025-06-26 20:46:20","cor":"orange"},
# {"lon":"-117.17484666666667","lat":"32.716791666666666","mmsi":"538071183","nome_navio":"GAME CHANGER","rumo":"275","id_origem_dados":"29","dh":"2025-06-26 20:51:59","cor":"yellow"},
# {"lon":"-94.337145","lat":"-6.5361","mmsi":"413548140","nome_navio":"NING FENG LENG 1","rumo":"34","id_origem_dados":"29","dh":"2025-06-26 20:55:40","cor":"yellow"},
# {"lon":"-89.09054666666667","lat":"30.359163333333335","mmsi":"257692000","nome_navio":"ARTEMIS ODYSSEY","rumo":"328","id_origem_dados":"29","dh":"2025-06-25 22:50:40","cor":"yellow"},
# {"lon":"-88.51098333333333","lat":"30.3428","mmsi":"368996000","nome_navio":"RONALD H BROWN","rumo":"14","id_origem_dados":"29","dh":"2025-06-26 02:49:22","cor":"yellow"},
# {"lon":"-87.79394333333333","lat":"26.664458333333332","mmsi":"311036200","nome_navio":"GLADIATOR","rumo":"312","id_origem_dados":"29","dh":"2025-06-26 16:54:46","cor":"orange"},
# {"lon":"-76.19882833333334","lat":"37.120326666666664","mmsi":"367258000","nome_navio":"CG SPENCER","rumo":"31","id_origem_dados":"29","dh":"2025-06-26 20:57:03","cor":"yellow"},
# {"lon":"-69.87716","lat":"18.471083333333333","mmsi":"538008283","nome_navio":"THALIS","rumo":"161","id_origem_dados":"29","dh":"2025-06-26 20:52:30","cor":"orange"},
# {"lon":"-69.24386333333334","lat":"12.18695","mmsi":"374104000","nome_navio":"LONGEVO","rumo":"126","id_origem_dados":"29","dh":"2025-06-26 20:56:51","cor":"yellow"},
# {"lon":"-68.885","lat":"13.385000000000002","mmsi":"374867000","nome_navio":"EVEREST","rumo":"341","id_origem_dados":"29","dh":"2025-06-26 18:55:44","cor":"yellow"},
# {"lon":"-64.08087","lat":"10.8699","mmsi":"677038700","nome_navio":"ANNA I","rumo":"70","id_origem_dados":"29","dh":"2025-06-26 18:05:37","cor":"orange"},
# {"lon":"-63.72338833333333","lat":"-8.568851666666667","mmsi":"710000918","nome_navio":"BERTOLINI L","rumo":"37.1","id_origem_dados":"29","dh":"2025-06-24 02:45:31","cor":"yellow"},
# {"lon":"-63.038333333333334","lat":"17.775000000000002","mmsi":"538005923","nome_navio":"GEO RESOLUTION","rumo":"125","id_origem_dados":"29","dh":"2025-06-26 12:46:58","cor":"yellow"},
# {"lon":"-61.63056","lat":"10.618371666666667","mmsi":"311070100","nome_navio":"ARGEO SEARCHER","rumo":"352","id_origem_dados":"29","dh":"2025-06-26 20:50:22","cor":"yellow"},
# {"lon":"-60.705065","lat":"-46.8713","mmsi":"412329694","nome_navio":"LU QING YUAN YU 212","rumo":"211","id_origem_dados":"29","dh":"2025-06-26 20:55:31","cor":"orange"},
# {"lon":"-60.455215","lat":"10.03246","mmsi":"377901075","nome_navio":"MR ALEX","rumo":"241.8","id_origem_dados":"29","dh":"2025-06-26 18:53:57","cor":"yellow"},
# {"lon":"-60.44754","lat":"-46.65678833333333","mmsi":"412329686","nome_navio":"LU QING YUAN YU 205","rumo":"225","id_origem_dados":"29","dh":"2025-06-26 20:54:58","cor":"yellow"},
# {"lon":"-60.415416666666665","lat":"-46.34936166666667","mmsi":"412329689","nome_navio":"LU QING YUAN YU 208","rumo":"206","id_origem_dados":"29","dh":"2025-06-26 20:55:28","cor":"yellow"},
# {"lon":"-60.34112833333333","lat":"-46.311726666666665","mmsi":"412329692","nome_navio":"LU QING YUAN YU 210","rumo":"213","id_origem_dados":"29","dh":"2025-06-26 20:54:57","cor":"orange"},
# {"lon":"-55.84169","lat":"-4.201415","mmsi":"9130074","nome_navio":"SANSAO II","rumo":"55","id_origem_dados":"29","dh":"2025-06-26 18:26:19","cor":"orange"},
# {"lon":"-51.064056666666666","lat":"-0.003933333333333333","mmsi":"9118723","nome_navio":"NV CMDT SILVA","rumo":"31","id_origem_dados":"29","dh":"2025-06-26 16:04:05","cor":"yellow"},
# {"lon":"-51.001488333333334","lat":"-2.193265","mmsi":"9129348","nome_navio":"ONWA29348","rumo":"216","id_origem_dados":"29","dh":"2025-06-26 21:43:29","cor":"yellow"},
# {"lon":"-50.941901666666666","lat":"2.8075833333333335","mmsi":"9126720","nome_navio":"ONWA26720","rumo":"0","id_origem_dados":"29","dh":"2025-06-26 20:45:12","cor":"orange"},
# {"lon":"-50.808971666666665","lat":"-1.3607633333333333","mmsi":"9128494","nome_navio":"ONWA28494","rumo":"342","id_origem_dados":"29","dh":"2025-06-26 18:26:03","cor":"orange"},
# {"lon":"-49.51586666666667","lat":"-50.4834","mmsi":"273211110","nome_navio":"PAMYAT ILICHA","rumo":"313","id_origem_dados":"29","dh":"2025-06-26 20:55:12","cor":"yellow"},
# {"lon":"-49.329161666666664","lat":"-1.6219999999999999","mmsi":"9118651","nome_navio":"BM FE EM DEUS","rumo":"266","id_origem_dados":"29","dh":"2025-06-26 02:15:35","cor":"yellow"},
# {"lon":"-48.992331666666665","lat":"8.679033333333333","mmsi":"775993100","nome_navio":"ADONE","rumo":"358","id_origem_dados":"29","dh":"2025-06-26 20:56:02","cor":"yellow"},
# {"lon":"-48.79680833333333","lat":"-1.5529516666666667","mmsi":"372977000","nome_navio":"ORCHID","rumo":"142.9","id_origem_dados":"29","dh":"2025-06-26 21:46:01","cor":"orange"},
# {"lon":"-48.506275","lat":"-1.558025","mmsi":"9130831","nome_navio":"ONWA30831","rumo":"260","id_origem_dados":"29","dh":"2025-06-25 06:30:48","cor":"orange"},
# {"lon":"-48.48271","lat":"-1.36085","mmsi":"9138508","nome_navio":"","rumo":"186","id_origem_dados":"29","dh":"2025-06-26 13:58:00","cor":"orange"},
# {"lon":"-48.18324666666667","lat":"-27.368643333333335","mmsi":"712345679","nome_navio":"0SMAR LUIS M_TIULEI_","rumo":"204","id_origem_dados":"29","dh":"2025-06-23 23:32:57","cor":"yellow"},
# {"lon":"-47.51280666666667","lat":"-25.919561666666667","mmsi":"710783460","nome_navio":"GRAN MAR","rumo":"246","id_origem_dados":"29","dh":"2025-06-26 21:38:01","cor":"yellow"},
# {"lon":"-47.42418833333333","lat":"-25.658521666666665","mmsi":"9128754","nome_navio":"ONWA28754","rumo":"227","id_origem_dados":"29","dh":"2025-06-26 20:52:36","cor":"orange"},
# {"lon":"-46.93207666666667","lat":"-24.57717","mmsi":"717182008","nome_navio":"CIGANO DO MAR 3","rumo":"221","id_origem_dados":"29","dh":"2025-06-26 21:03:51","cor":"yellow"},
# {"lon":"-46.572903333333336","lat":"-24.330653333333334","mmsi":"717182011","nome_navio":"PACIFICO 3","rumo":"23","id_origem_dados":"29","dh":"2025-06-24 12:11:00","cor":"yellow"},
# {"lon":"-46.481335","lat":"-25.16803833333333","mmsi":"9129190","nome_navio":"MARAVILHOSO","rumo":"114","id_origem_dados":"29","dh":"2025-06-26 21:41:08","cor":"yellow"},
# {"lon":"-46.32189","lat":"-23.996486666666666","mmsi":"710355896","nome_navio":"PEREIRA LIMA II GIJO","rumo":"238.5","id_origem_dados":"29","dh":"2025-06-26 20:02:02","cor":"orange"},
# {"lon":"-46.26171333333333","lat":"-24.160593333333335","mmsi":"538010199","nome_navio":"IONIAN SEA","rumo":"81","id_origem_dados":"29","dh":"2025-06-26 21:36:52","cor":"yellow"},
# {"lon":"-46.217346666666664","lat":"-24.090728333333335","mmsi":"636020328","nome_navio":"MEL GRACE","rumo":"81","id_origem_dados":"29","dh":"2025-06-26 21:38:07","cor":"orange"},
# {"lon":"-46.20054833333333","lat":"-24.131506666666667","mmsi":"9129203","nome_navio":"GAROPAO 2","rumo":"59","id_origem_dados":"29","dh":"2025-06-26 21:15:41","cor":"yellow"},
# {"lon":"-46.16608166666666","lat":"-29.500276666666668","mmsi":"710000124","nome_navio":"B2 CAROLINA F 87_","rumo":"80","id_origem_dados":"29","dh":"2025-06-26 20:38:09","cor":"yellow"},
# {"lon":"-46.010866666666665","lat":"-24.211916666666667","mmsi":"9129208","nome_navio":"ONWA 8","rumo":"188","id_origem_dados":"29","dh":"2025-06-26 10:22:51","cor":"orange"},
# {"lon":"-44.64167166666667","lat":"-23.183943333333332","mmsi":"9129185","nome_navio":"RUA AZUZA","rumo":"256","id_origem_dados":"29","dh":"2025-06-25 12:19:28","cor":"yellow"},
# {"lon":"-44.62459666666667","lat":"-23.26754","mmsi":"9129196","nome_navio":"MONTE CARMELO","rumo":"328","id_origem_dados":"29","dh":"2025-06-26 19:38:56","cor":"yellow"},
# {"lon":"-44.529736666666665","lat":"-23.361183333333333","mmsi":"152924335","nome_navio":"B CONFIANCA MC","rumo":"245","id_origem_dados":"29","dh":"2025-06-26 21:07:04","cor":"yellow"},
# {"lon":"-44.34264","lat":"-2.3999916666666667","mmsi":"613579000","nome_navio":"TEMIRO","rumo":"168","id_origem_dados":"29","dh":"2025-06-26 21:44:33","cor":"orange"},
# {"lon":"-43.333146666666664","lat":"-23.222198333333335","mmsi":"711233343","nome_navio":"DONA FLOR F","rumo":"85.3","id_origem_dados":"29","dh":"2025-06-26 00:53:06","cor":"yellow"},
# {"lon":"-43.17754166666667","lat":"-23.047238333333333","mmsi":"9131032","nome_navio":"VASCOJR","rumo":"265","id_origem_dados":"29","dh":"2025-06-26 12:37:32","cor":"yellow"},
# {"lon":"-43.133993333333336","lat":"-22.841951666666667","mmsi":"538010990","nome_navio":"OCEAN VANGUARD","rumo":"28","id_origem_dados":"29","dh":"2025-06-26 21:39:06","cor":"yellow"},
# {"lon":"-43.11987666666667","lat":"-22.8797","mmsi":"9124952","nome_navio":"ONWA24952","rumo":"0","id_origem_dados":"29","dh":"2025-06-26 08:45:27","cor":"orange"},
# {"lon":"-43.11185","lat":"-22.869348333333335","mmsi":"325141900","nome_navio":"SUSAN","rumo":"0","id_origem_dados":"29","dh":"2025-06-26 21:45:06","cor":"orange"},
# {"lon":"-43.095151666666666","lat":"-22.824166666666667","mmsi":"585992","nome_navio":"ELITE A","rumo":"219","id_origem_dados":"29","dh":"2025-06-26 21:24:13","cor":"yellow"},
# {"lon":"-43.09448","lat":"-22.82533","mmsi":"9131056","nome_navio":"FENIX V","rumo":"322","id_origem_dados":"29","dh":"2025-06-26 21:39:28","cor":"yellow"},
# {"lon":"-42.783163333333334","lat":"-25.168323333333333","mmsi":"236538000","nome_navio":"SANCO SPIRIT","rumo":"167","id_origem_dados":"29","dh":"2025-06-26 21:34:10","cor":"yellow"},
# {"lon":"-42.53794666666666","lat":"-24.815796666666667","mmsi":"311000819","nome_navio":"SEALOADER 2","rumo":"30","id_origem_dados":"29","dh":"2025-06-26 13:58:22","cor":"yellow"},
# {"lon":"-42.45616666666667","lat":"-24.566583333333334","mmsi":"210591000","nome_navio":"BOKA SUB C","rumo":"44","id_origem_dados":"29","dh":"2025-06-26 21:40:58","cor":"yellow"},
# {"lon":"-41.958935","lat":"-23.311901666666667","mmsi":"9129367","nome_navio":"FISH","rumo":"164","id_origem_dados":"29","dh":"2025-06-26 08:02:56","cor":"yellow"},
# {"lon":"-41.822466666666664","lat":"-22.767946666666667","mmsi":"9128489","nome_navio":"SHALOM 1","rumo":"55","id_origem_dados":"29","dh":"2025-06-25 09:10:03","cor":"yellow"},
# {"lon":"-41.751035","lat":"-22.796886666666666","mmsi":"40007502","nome_navio":"JOSE ALMIR","rumo":"39","id_origem_dados":"29","dh":"2025-06-25 12:57:10","cor":"yellow"},
# {"lon":"-41.180126666666666","lat":"-22.96169","mmsi":"232050912","nome_navio":"THOR II","rumo":"258","id_origem_dados":"29","dh":"2025-06-26 21:37:44","cor":"yellow"},
# {"lon":"-40.770455","lat":"-20.892131666666668","mmsi":"9131118","nome_navio":"RIO MAMORE","rumo":"0","id_origem_dados":"29","dh":"2025-06-25 08:12:26","cor":"orange"},
# {"lon":"-40.710701666666665","lat":"-22.482028333333332","mmsi":"711109117","nome_navio":"ESTRELA DO HORIZONTE","rumo":"27","id_origem_dados":"29","dh":"2025-06-26 21:06:22","cor":"yellow"},
# {"lon":"-40.70403666666667","lat":"-21.760473333333334","mmsi":"9128457","nome_navio":"ROUPA NOVA","rumo":"152","id_origem_dados":"29","dh":"2025-06-26 13:50:00","cor":"yellow"},
# {"lon":"-40.681869999999996","lat":"-22.955066666666667","mmsi":"209108000","nome_navio":"SW DUCHESS","rumo":"106","id_origem_dados":"29","dh":"2025-06-26 21:44:44","cor":"yellow"},
# {"lon":"-40.63333333333333","lat":"-23.416666666666668","mmsi":"257728000","nome_navio":"OCEANIC VEGA","rumo":"69","id_origem_dados":"29","dh":"2025-06-26 21:45:27","cor":"yellow"},
# {"lon":"-40.539746666666666","lat":"-20.817296666666667","mmsi":"9130065","nome_navio":"ONWA30065","rumo":"212","id_origem_dados":"29","dh":"2025-06-23 23:46:03","cor":"yellow"},
# {"lon":"-40.53558666666667","lat":"-0.38837666666666665","mmsi":"373731000","nome_navio":"CENTURIES","rumo":"26","id_origem_dados":"29","dh":"2025-06-26 19:45:17","cor":"yellow"},
# {"lon":"-40.3212","lat":"-20.324683333333333","mmsi":"351859000","nome_navio":"SEWARD JOHNSON","rumo":"181","id_origem_dados":"29","dh":"2025-06-26 10:15:17","cor":"yellow"},
# {"lon":"-39.82969666666666","lat":"-21.889911666666666","mmsi":"538011008","nome_navio":"GENESIS I","rumo":"30","id_origem_dados":"29","dh":"2025-06-26 21:05:19","cor":"yellow"},
# {"lon":"-39.25","lat":"0","mmsi":"9129216","nome_navio":"DECISAO","rumo":"6","id_origem_dados":"29","dh":"2025-06-26 11:13:49","cor":"yellow"},
# {"lon":"-39.22359","lat":"-17.344698333333334","mmsi":"9126893","nome_navio":"AYRTON SENNA","rumo":"334","id_origem_dados":"29","dh":"2025-06-26 20:16:00","cor":"yellow"},
# {"lon":"-39.11145166666667","lat":"-18.62675","mmsi":"9127686","nome_navio":"CAIAGO","rumo":"29","id_origem_dados":"29","dh":"2025-06-26 21:27:34","cor":"yellow"},
# {"lon":"-38.83585","lat":"-21.038016666666667","mmsi":"314978000","nome_navio":"ENIGMA","rumo":"51","id_origem_dados":"29","dh":"2025-06-26 21:45:34","cor":"red"},
# {"lon":"-38.691698333333335","lat":"-14.059066666666666","mmsi":"9126920","nome_navio":"BRAPESCA 2","rumo":"127","id_origem_dados":"29","dh":"2025-06-26 16:04:08","cor":"yellow"},
# {"lon":"-38.579215","lat":"-14.03695","mmsi":"9129356","nome_navio":"RIO AMAZONAS","rumo":"177","id_origem_dados":"29","dh":"2025-06-26 21:45:40","cor":"yellow"},
# {"lon":"-38.493853333333334","lat":"-15.750778333333333","mmsi":"710785543","nome_navio":"CELEBRIDADE _ B6","rumo":"234.3","id_origem_dados":"29","dh":"2025-06-26 17:15:57","cor":"yellow"},
# {"lon":"-38.47166666666667","lat":"-19.976666666666667","mmsi":"636017184","nome_navio":"BULK COLOMBIA","rumo":"219","id_origem_dados":"29","dh":"2025-06-26 21:44:23","cor":"orange"},
# {"lon":"-36.092905","lat":"-11.285378333333334","mmsi":"311001279","nome_navio":"FUGRO RESILIENCE","rumo":"198","id_origem_dados":"29","dh":"2025-06-26 21:46:07","cor":"yellow"},
# {"lon":"-35.72879833333333","lat":"-9.682485","mmsi":"232046145","nome_navio":"FUGRO VAQUITA","rumo":"205","id_origem_dados":"29","dh":"2025-06-26 05:18:04","cor":"yellow"},
# {"lon":"-35.475705","lat":"0.4727","mmsi":"91800028","nome_navio":"ONWA33NT 91_","rumo":"320","id_origem_dados":"29","dh":"2025-06-26 19:17:33","cor":"yellow"},
# {"lon":"-35.206066666666665","lat":"-5.774023333333333","mmsi":"246550000","nome_navio":"CAP CROISETTE","rumo":"206","id_origem_dados":"29","dh":"2025-06-26 21:44:10","cor":"orange"},
# {"lon":"-34.867733333333334","lat":"-8.055045","mmsi":"636019265","nome_navio":"PORT OSAKA","rumo":"198","id_origem_dados":"29","dh":"2025-06-26 21:00:37","cor":"orange"},
# {"lon":"-32.96415","lat":"-6.039416666666667","mmsi":"613003808","nome_navio":"MT SAURI","rumo":"215","id_origem_dados":"29","dh":"2025-06-26 21:45:14","cor":"orange"},
# {"lon":"-32.877255","lat":"-10.231371666666666","mmsi":"371632000","nome_navio":"MAWASHI EXPRESS","rumo":"30","id_origem_dados":"29","dh":"2025-06-26 21:44:54","cor":"yellow"},
# {"lon":"-32.66548","lat":"-1.25676","mmsi":"9128422","nome_navio":"ONWA28422","rumo":"130","id_origem_dados":"29","dh":"2025-06-26 21:08:05","cor":"yellow"},
# {"lon":"-31.833721666666666","lat":"-1.5685333333333333","mmsi":"9135339","nome_navio":"","rumo":"256","id_origem_dados":"29","dh":"2025-06-24 09:58:02","cor":"yellow"},
# {"lon":"-31.530106666666665","lat":"-1.483515","mmsi":"9135337","nome_navio":"","rumo":"111","id_origem_dados":"29","dh":"2025-06-26 21:34:56","cor":"yellow"},
# {"lon":"-25.663565","lat":"37.73763666666667","mmsi":"538071658","nome_navio":"SHINKAI","rumo":"238","id_origem_dados":"29","dh":"2025-06-26 20:56:13","cor":"orange"},
# {"lon":"-24.138333333333335","lat":"48.22166666666667","mmsi":"235093069","nome_navio":"BERGE TOWNSEND","rumo":"259","id_origem_dados":"29","dh":"2025-06-26 20:53:47","cor":"yellow"},
# {"lon":"-20.15585","lat":"12.334999999999999","mmsi":"538006684","nome_navio":"B.SUN","rumo":"323","id_origem_dados":"29","dh":"2025-06-26 20:55:08","cor":"yellow"},
# {"lon":"-19.598203333333334","lat":"-27.989518333333333","mmsi":"227891680","nome_navio":"AVEL","rumo":"120","id_origem_dados":"29","dh":"2025-06-26 12:08:08","cor":"red"},
# {"lon":"-18.739938333333335","lat":"1.51949","mmsi":"204235000","nome_navio":"MONSERRATE","rumo":"205","id_origem_dados":"29","dh":"2025-06-26 20:56:10","cor":"yellow"},
# {"lon":"-17.431566666666665","lat":"14.6867","mmsi":"412331032","nome_navio":"LUQINGYUAN027","rumo":"166.7","id_origem_dados":"29","dh":"2025-06-26 20:56:22","cor":"yellow"},
# {"lon":"-11.470883333333333","lat":"41.04609833333333","mmsi":"314001015","nome_navio":"DERIN","rumo":"193","id_origem_dados":"29","dh":"2025-06-26 20:49:14","cor":"orange"},
# {"lon":"-10.699196666666667","lat":"34.34658833333334","mmsi":"511101742","nome_navio":"FLORA 1","rumo":"66","id_origem_dados":"29","dh":"2025-06-26 20:56:12","cor":"orange"},
# {"lon":"-10.218333333333334","lat":"-8.068333333333333","mmsi":"257908000","nome_navio":"SW EMPRESS","rumo":"64","id_origem_dados":"29","dh":"2025-06-26 21:46:18","cor":"yellow"},
# {"lon":"-5.893166666666667","lat":"35.899","mmsi":"224886000","nome_navio":"HESPERIDES","rumo":"90","id_origem_dados":"29","dh":"2025-06-26 20:57:00","cor":"yellow"},
# {"lon":"-4.020296666666667","lat":"5.297658333333334","mmsi":"353424000","nome_navio":"AMIS INTEGRITY","rumo":"166","id_origem_dados":"29","dh":"2025-06-26 20:54:16","cor":"orange"},
# {"lon":"-0.19503333333333334","lat":"53.637616666666666","mmsi":"538007556","nome_navio":"GOLDEN AMBER","rumo":"319","id_origem_dados":"29","dh":"2025-06-26 20:46:44","cor":"yellow"},
# {"lon":"0.007395","lat":"5.62806","mmsi":"311000854","nome_navio":"FUGRO SUPPORTER","rumo":"219","id_origem_dados":"29","dh":"2025-06-26 20:53:00","cor":"yellow"},
# {"lon":"1.9500000000000002","lat":"59.40166666666667","mmsi":"259073000","nome_navio":"HAVILA SUBSEA","rumo":"274","id_origem_dados":"29","dh":"2025-06-26 19:29:59","cor":"yellow"},
# {"lon":"2.245","lat":"62.20166666666667","mmsi":"311000275","nome_navio":"OCEAN MERMAID","rumo":"78","id_origem_dados":"29","dh":"2025-06-26 20:42:39","cor":"yellow"},
# {"lon":"3.3508883333333332","lat":"51.818223333333336","mmsi":"667002087","nome_navio":"MATIN BEY","rumo":"269","id_origem_dados":"29","dh":"2025-06-26 20:06:15","cor":"orange"},
# {"lon":"4.2574266666666665","lat":"51.291558333333334","mmsi":"636021363","nome_navio":"MSC EUGENIA","rumo":"32","id_origem_dados":"29","dh":"2025-06-26 20:52:52","cor":"yellow"},
# {"lon":"4.705","lat":"64.19333333333334","mmsi":"244679599","nome_navio":"WITNESS","rumo":"335","id_origem_dados":"29","dh":"2025-06-26 20:52:56","cor":"yellow"},
# {"lon":"5.049948333333333","lat":"61.610546666666664","mmsi":"311056100","nome_navio":"APOLLO","rumo":"70","id_origem_dados":"29","dh":"2025-06-26 20:51:04","cor":"yellow"},
# {"lon":"5.842613333333333","lat":"78.22081166666666","mmsi":"211202460","nome_navio":"POLARSTERN","rumo":"157","id_origem_dados":"29","dh":"2025-06-26 20:50:43","cor":"yellow"},
# {"lon":"7.009628333333334","lat":"4.770561666666667","mmsi":"371410000","nome_navio":"ULTRA HANDY","rumo":"351","id_origem_dados":"29","dh":"2025-06-26 20:51:27","cor":"orange"},
# {"lon":"7.123333333333334","lat":"65.45166666666667","mmsi":"258054000","nome_navio":"RAMFORM VICTORY","rumo":"317","id_origem_dados":"29","dh":"2025-06-26 20:55:51","cor":"yellow"},
# {"lon":"8.020000000000001","lat":"-3.441666666666667","mmsi":"306881000","nome_navio":"ARTIKE","rumo":"303","id_origem_dados":"29","dh":"2025-06-26 20:54:27","cor":"orange"},
# {"lon":"12.132831666666666","lat":"56.74834","mmsi":"372837000","nome_navio":"BALTIYSKIY_202","rumo":"167","id_origem_dados":"29","dh":"2025-06-26 20:57:00","cor":"red"},
# {"lon":"14.77235","lat":"35.89215","mmsi":"636014046","nome_navio":"HINOKI","rumo":"349","id_origem_dados":"29","dh":"2025-06-26 20:56:28","cor":"orange"},
# {"lon":"18.59127","lat":"-35.01405666666667","mmsi":"256276000","nome_navio":"WILFORCE","rumo":"109","id_origem_dados":"29","dh":"2025-06-26 20:53:30","cor":"yellow"},
# {"lon":"23.894433333333332","lat":"59.624335","mmsi":"273359440","nome_navio":"AKADEMIK TRYOSHNIKOV","rumo":"72","id_origem_dados":"29","dh":"2025-06-26 20:56:14","cor":"orange"},
# {"lon":"25.427353333333333","lat":"-36.837246666666665","mmsi":"563112900","nome_navio":"WINNER 6","rumo":"285","id_origem_dados":"29","dh":"2025-06-26 20:53:02","cor":"yellow"},
# {"lon":"26.53315","lat":"36.70896666666667","mmsi":"352001610","nome_navio":"AYDOS","rumo":"309","id_origem_dados":"29","dh":"2025-06-26 20:56:43","cor":"orange"},
# {"lon":"27.914976666666668","lat":"43.191118333333335","mmsi":"207506400","nome_navio":"NAVAL RSV 421","rumo":"276","id_origem_dados":"29","dh":"2025-06-26 20:51:13","cor":"yellow"},
# {"lon":"28.979036666666666","lat":"40.81481","mmsi":"352003750","nome_navio":"TEAM","rumo":"355.3","id_origem_dados":"29","dh":"2025-06-26 20:52:17","cor":"orange"},
# {"lon":"29.2276","lat":"40.83606666666667","mmsi":"613744000","nome_navio":"LIDER HALUK","rumo":"84","id_origem_dados":"29","dh":"2025-06-26 19:28:20","cor":"orange"},
# {"lon":"30.079141666666665","lat":"31.334748333333334","mmsi":"538009398","nome_navio":"IPPOKRATIS","rumo":"346","id_origem_dados":"29","dh":"2025-06-26 20:52:45","cor":"yellow"},
# {"lon":"35.857755","lat":"34.50204333333333","mmsi":"667001462","nome_navio":"OSMAN BEY","rumo":"170","id_origem_dados":"29","dh":"2025-06-26 20:47:14.76","cor":"orange"},
# {"lon":"36.60719","lat":"44.8847","mmsi":"352001034","nome_navio":"ZAMBRA","rumo":"199","id_origem_dados":"29","dh":"2025-06-26 07:46:42","cor":"orange"},
# {"lon":"39.64333333333333","lat":"-4.046146666666667","mmsi":"314556000","nome_navio":"TRUE MARINER","rumo":"335","id_origem_dados":"29","dh":"2025-06-26 20:47:44","cor":"yellow"},
# {"lon":"41.88449333333333","lat":"-28.890125","mmsi":"994008686","nome_navio":"YJC_BUOY_026 9V","rumo":"252.6","id_origem_dados":"29","dh":"2025-06-26 15:30:13","cor":"yellow"},
# {"lon":"43.60801","lat":"-12.389775","mmsi":"228379700","nome_navio":"PLASTIC ODYSSEY","rumo":"320","id_origem_dados":"29","dh":"2025-06-26 20:55:48","cor":"yellow"},
# {"lon":"49.03754166666667","lat":"-9.798068333333333","mmsi":"371462000","nome_navio":"CHEMROAD ROSE","rumo":"28","id_origem_dados":"29","dh":"2025-06-26 20:56:13","cor":"yellow"},
# {"lon":"50.402438333333336","lat":"13.523666666666667","mmsi":"314834000","nome_navio":"EVEREST","rumo":"75","id_origem_dados":"29","dh":"2025-06-26 20:52:48","cor":"yellow"},
# {"lon":"56.115226666666665","lat":"-32.69336333333333","mmsi":"224609000","nome_navio":"NUEVO GOLONDRINA","rumo":"336","id_origem_dados":"29","dh":"2025-06-26 20:56:11","cor":"yellow"},
# {"lon":"56.60659166666667","lat":"25.671931666666666","mmsi":"352001425","nome_navio":"OCEAN AUTUMN","rumo":"179","id_origem_dados":"29","dh":"2025-06-26 20:42:46","cor":"yellow"},
# {"lon":"56.61643","lat":"26.666558333333334","mmsi":"341365000","nome_navio":"RASHA","rumo":"326","id_origem_dados":"29","dh":"2025-06-26 18:57:04","cor":"orange"},
# {"lon":"57.100863333333336","lat":"-21.101251666666666","mmsi":"314509000","nome_navio":"OTHRYS","rumo":"241","id_origem_dados":"29","dh":"2025-06-26 20:55:35","cor":"orange"},
# {"lon":"58.064483333333335","lat":"12.759935","mmsi":"305703000","nome_navio":"O7 VEGA S","rumo":"180","id_origem_dados":"29","dh":"2025-06-26 20:43:47","cor":"yellow"},
# {"lon":"61.26833333333334","lat":"12.200000000000001","mmsi":"352003390","nome_navio":"SINO PROSPERITY","rumo":"293","id_origem_dados":"29","dh":"2025-06-26 20:53:53","cor":"orange"},
# {"lon":"63.600055","lat":"-15.635593333333333","mmsi":"636019542","nome_navio":"ML HERON","rumo":"60","id_origem_dados":"29","dh":"2025-06-26 20:51:06","cor":"orange"},
# {"lon":"67.34784166666667","lat":"14.692856666666666","mmsi":"636019822","nome_navio":"AMIS UNICORN","rumo":"294","id_origem_dados":"29","dh":"2025-06-26 06:52:49","cor":"orange"},
# {"lon":"73.08833333333334","lat":"17.32166666666667","mmsi":"636022705","nome_navio":"ETOILE","rumo":"277","id_origem_dados":"29","dh":"2025-06-26 00:06:16","cor":"yellow"},
# {"lon":"77.87","lat":"-10.07","mmsi":"626227000","nome_navio":"VIEIRA","rumo":"50","id_origem_dados":"29","dh":"2025-06-26 20:55:17","cor":"orange"},
# {"lon":"96.20500000000001","lat":"7.195","mmsi":"538007505","nome_navio":"GROTON EAGLE","rumo":"127","id_origem_dados":"29","dh":"2025-06-26 20:54:43","cor":"orange"},
# {"lon":"104.02693166666667","lat":"10.075255","mmsi":"900000000","nome_navio":"ESCRAVOS PILOT","rumo":"348","id_origem_dados":"29","dh":"2025-06-26 10:07:53","cor":"yellow"},
# {"lon":"114.08767166666667","lat":"22.332923333333333","mmsi":"477836700","nome_navio":"JOSCO DAZHOU","rumo":"58.7","id_origem_dados":"29","dh":"2025-06-26 20:56:40","cor":"orange"},
# {"lon":"115.145","lat":"4.991388333333333","mmsi":"18","nome_navio":"LONGLINE BUOY 18_46_","rumo":"0","id_origem_dados":"29","dh":"2025-06-26 00:02:00","cor":"yellow"},
# {"lon":"120.95619166666667","lat":"31.76666","mmsi":"538007025","nome_navio":"TS GOLF","rumo":"268","id_origem_dados":"29","dh":"2025-06-26 20:48:29","cor":"orange"},
# {"lon":"121.99147666666667","lat":"35.57068","mmsi":"538008955","nome_navio":"DORYSIA","rumo":"357","id_origem_dados":"29","dh":"2025-06-26 17:23:15","cor":"orange"},
# {"lon":"122.36606166666667","lat":"30.971306666666667","mmsi":"244868000","nome_navio":"NORDIC","rumo":"279","id_origem_dados":"29","dh":"2025-06-26 20:51:51","cor":"yellow"},
# {"lon":"123.36000000000001","lat":"24.408333333333335","mmsi":"352001232","nome_navio":"RIQUEZA","rumo":"204","id_origem_dados":"29","dh":"2025-06-26 20:51:22","cor":"yellow"},
# {"lon":"124.31101666666666","lat":"29.166633333333333","mmsi":"636024276","nome_navio":"MANZANILLO","rumo":"32","id_origem_dados":"29","dh":"2025-06-26 18:13:27","cor":"yellow"},
# {"lon":"124.3423","lat":"27.724891666666668","mmsi":"538004169","nome_navio":"SEAWAYS KILIMANJARO","rumo":"194","id_origem_dados":"29","dh":"2025-06-26 20:43:00","cor":"yellow"},
# {"lon":"126.91666666666667","lat":"29.041666666666668","mmsi":"636017781","nome_navio":"APOLLON","rumo":"139","id_origem_dados":"29","dh":"2025-06-26 20:47:42","cor":"yellow"},
# {"lon":"127.49818333333333","lat":"25.799796666666666","mmsi":"668116267","nome_navio":"B MARU 8","rumo":"239.4","id_origem_dados":"29","dh":"2025-06-24 13:29:59","cor":"orange"},
# {"lon":"130.115845","lat":"30.571695","mmsi":"354424000","nome_navio":"YACHIYO","rumo":"255","id_origem_dados":"29","dh":"2025-06-26 03:26:24","cor":"yellow"},
# {"lon":"130.88113666666666","lat":"-34.98264666666667","mmsi":"229625000","nome_navio":"MSC AJACCIO","rumo":"115","id_origem_dados":"29","dh":"2025-06-26 20:56:26","cor":"yellow"},
# {"lon":"152.06133833333334","lat":"-32.700828333333334","mmsi":"710000164","nome_navio":"LUTHIER","rumo":"8.3","id_origem_dados":"29","dh":"2025-06-26 21:40:39","cor":"yellow"}]""")


resultados = []

# 2. Para cada navio, obter detalhes
for emb in embarcacoes:
    mmsi = emb["mmsi"]
    nome_navio = emb["nome_navio"]
    lat = emb["lat"]
    lon = emb["lon"]
    cor = emb["cor"]

    #{"lon":"-40.543146666666665","lat":"-0.4037516666666667",
    # "mmsi":"373731000","nome_navio":"CENTURIES",
    # "rumo":"26",
    # "id_origem_dados":"29","dh":"2025-06-26 14:36:46",
    # "cor":"yellow"},
    url_detalhe = f"http://10.205.144.95/sistram5/includes/CardMeio.php?mmsi={mmsi}&id_usuario=0001"
    resp = requests.get(url_detalhe, proxies=proxies)
    soup = BeautifulSoup(resp.content, "html.parser")

    # Dados da tabela
    dados = {}
    tabela = soup.find("table", class_="table table-striped table-bordered")
    if tabela:
        for tr in tabela.find_all("tr"):
            th = tr.find("th")
            td = tr.find("td")
            if th and td:
                dados[th.text.strip()] = td.text.strip()

    # Observação atual
    obs_input = soup.select_one("input#obsnaesp")
    obs_valor = obs_input["value"] if obs_input and "value" in obs_input.attrs else ""

    # Histórico
    historico_naesp = []
    for ta in soup.select("#collapseExample6 textarea")[:3]:
        texto = ta.text.strip()
        match = re.search(r"Obs:\s*(.*)", texto, re.DOTALL)
        if match:
            obs = match.group(1).strip()
            historico_naesp.append(obs)
    
    # Capturar IMO, se existir na tabela
    imo = dados.get("IMO", "")
    #print(historico_naesp)
    # Montar resultado
    resultados.append({
        "nome_navio": nome_navio,
        "mmsi": mmsi,
        "imo": imo,  # <-- aqui
        "coordenadas": {"lat": lat, "lon": lon},
        "dados": dados,
        "naesp_obs": obs_valor,
        "classificação": cor,
        "naesp_historico": historico_naesp
    })

# 3. HTML com mapa
html_template = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Mapa de Embarcações</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
    <style>
        #map {{ height: 100vh; }}
        .popup-content {{ max-width: 500px; }}
        .popup-content textarea {{ width: 100%; height: 100px; }}
        .marker-box {{background: rgba(255, 255, 255, 0.8);
                      border: 2px solid gray;padding: 4px 6px;
                      border-radius: 6px;font-size: 12px;
                      font-weight: bold;color: #333;}}
        .popup-content img {{border: 1px solid #ccc;box-shadow: 1px 1px 4px rgba(0,0,0,0.2);}}
    </style>
</head>
<body>
<div id="map"></div>

<script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
<script>
    let embarcacoes = {json.dumps(resultados, indent=2, ensure_ascii=False)};

    let map = L.map('map').setView([-15, -45], 5);

    L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png', {{
        attribution: 'Leaflet & OpenStreetMap'
    }}).addTo(map);
   // Define a área SAR como um polígono
    const areaSAR3DN = L.polygon([
        [-2.9217,-41.2676], [7.6664,-35], [-6.3667,-16], [-6.3667,-10],
        [-20.6608,-10], [-10.5,-36.4167], [-10.0019,-37.0818], [-9.5472,-37.8618],
        [-8.8097,-38.9605], [-8.8314,-39.8174], [-9.363,-40.3228], [-9.4497,-40.7293],
        [-8.9291,-40.8721], [-8.7337,-41.2786], [-7.766,-40.6633], [-7.3631,-40.6963],
        [-6.7743,-40.4107], [-6.5561,-40.7402], [-5.5729,-41.0698], [-4.6318,-41.2236],
        [-3.4921,-41.4653], [-2.9217,-41.2676]
    ], {{color: "red",fillOpacity: 0.05, weight: 2}}).addTo(map);

    // Adiciona os navios se estiverem dentro da área SAR
    embarcacoes.forEach(emb => {{
        const latlng = L.latLng(parseFloat(emb.coordenadas.lat), parseFloat(emb.coordenadas.lon));
        const imagemUrl = emb.mmsi
                ? `https://photos.marinetraffic.com/ais/showphoto.aspx?mmsi=${{emb.mmsi}}` 
                : (emb.imo ? `https://photos.marinetraffic.com/ais/showphoto.aspx?imo=${{emb.imo}}` : '');

        



        if (areaSAR3DN.getBounds().contains(latlng)) {{
            const popupHTML = `
                <div class="popup-content">
                    <strong>${{emb.nome_navio}}</strong><br>
                    ${{Object.entries(emb.dados).map(([k,v]) => `<b>${{k}}:</b> ${{v}}<br>`).join("")}}
                    <b>Histórico (NAESP):</b><br>
                    ${{emb.naesp_historico.slice(0, 3).map(h => `${{h}}`).join("<br><br>")}}
                </div>
            `;

            let cor = "green";
            if (emb.classificação.toLowerCase().includes("red")) cor = "red";
            else if (emb.classificação.toLowerCase().includes("orange")) cor = "orange";
            else if (emb.classificação.toLowerCase().includes("yellow")) cor = "yellow";

            const icon = L.divIcon({{className: 'custom-marker',html: 
            `<div class="marker-box" style="border-color:${{cor}}; display: flex; align-items: flex-start;">
            <div style="flex: 1;">
                ${{Object.entries(emb.dados).map(([k,v]) => `<b>${{k}}:</b> ${{v}}<br>`).join("")}}
                    <b>Histórico (NAESP):</b><br>
                    ${{emb.naesp_historico.slice(0, 3).map(h => `${{h}}`).join("<br><br>")}}
            </div>
            ${{imagemUrl ? `<img src="${{imagemUrl}}" style="width: 100px; height: auto; margin-left: 10px; border-radius: 4px;" onerror="this.style.display='none';">` : ""}}
        </div>`,iconSize: [400, 120],iconAnchor: [30, 15]}});
             const marcador = L.marker(latlng, {{ icon: icon, draggable: true }}).addTo(map);
            marcador.bindPopup(popupHTML);
            // Linha fixa da posição inicial
            const linha = L.polyline([latlng, latlng], {{ color: cor }}).addTo(map);
             marcador.on('drag', function (event) {{
                const novaPosicao = event.target.getLatLng();
                linha.setLatLngs([latlng, novaPosicao]);}});
            L.circleMarker(latlng, {{radius: 8,color: cor,fillColor: cor,fillOpacity: 0.8,weight: 1}}).addTo(map).bindPopup(popupHTML);


        }}
    }});
</script>
</body>
</html>
"""

# 4. Salvar
with open("Sitrep_Naesp.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print("✔️ Mapa salvo como mapa_navios3.html")
