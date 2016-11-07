import math
import matplotlib.pyplot as plt
import statistics as stats

chicago_6b_300d = "0.37692 -0.10618 -0.44225 0.15333 -0.1678 0.45699 -0.39608 0.016068 0.070837 0.12977 0.15717 0.17619 0.15231 0.11057 0.62411 0.037107 0.1652 -0.1529 0.10264 -0.12403 -0.80791 -0.41285 -0.034949 0.035587 0.21259 0.16847 -0.27894 0.064389 -0.49085 -0.67298 0.015538 0.20814 -0.18912 -0.070057 -1.5028 0.039156 0.13115 0.237 -0.38295 -0.18368 0.13609 -0.090485 -0.20953 0.81182 -0.2722 0.29417 -0.0074806 -0.1206 -0.26657 0.21967 0.1094 0.36381 -0.44351 0.12258 0.37327 -0.5311 0.062191 -0.08614 -0.18671 -0.88763 -0.56986 0.64322 0.53241 -0.1324 -0.057253 -0.024162 0.24634 0.025937 0.092236 -0.34064 0.65191 -0.39996 -0.26812 -0.14901 -0.53872 -0.32514 -0.0047088 0.80628 0.14315 0.15366 -0.82966 0.13511 -0.18134 -0.19444 -0.22894 -0.089837 -0.25277 0.019884 -0.39674 0.45762 0.4965 0.21166 0.22275 0.061238 -0.20984 0.010427 -0.49564 -0.14778 -0.4082 -0.86303 0.14691 0.044392 0.038488 -0.14005 -0.29404 0.040919 0.086697 0.38477 0.26583 0.33572 -0.68046 -0.67915 -0.21631 0.036965 -0.020145 0.18438 -0.12363 0.053634 -0.047044 0.21794 0.44687 -0.33515 0.060189 -0.11936 -0.1012 -0.66593 0.63813 -0.11019 0.1371 -0.43708 0.22756 0.041059 0.31386 -0.31223 -0.076634 0.31134 -0.30968 -0.21259 0.1512 0.28623 -0.19029 0.12009 -0.38754 0.50059 0.22772 0.17957 -0.076966 -0.099864 -0.32838 -0.13568 0.97576 0.25664 0.16672 0.098172 0.18665 0.27716 0.35612 -0.043168 -0.21648 -0.02105 0.5382 0.24695 -0.36215 -0.079124 0.22389 0.19967 -0.072162 -0.40156 0.12399 0.25024 -0.047885 -0.22885 -1.0609 0.30483 0.40839 -0.088072 0.42854 -0.22994 -0.54981 0.064667 0.23534 0.77524 -0.24256 0.32131 -0.23095 0.30596 -0.6715 -0.53017 -0.24432 -0.044854 -0.022036 0.14451 -0.043094 0.0063234 -0.36577 -0.91867 0.19973 -0.32619 0.095966 0.082448 0.98079 -0.074722 0.73787 0.078189 -0.64466 0.052939 0.0096951 0.63615 0.16776 -0.49792 0.075412 -0.30745 -0.4247 0.058197 -0.037567 0.38795 -0.055177 -0.11412 -0.049433 -0.90722 0.66266 -0.069863 0.026911 -0.18684 -0.10865 -0.020772 -0.6135 0.34503 0.052312 -0.13749 0.015537 0.49881 -0.23448 0.15751 -0.53532 -0.13938 0.31478 -0.052328 -0.61115 0.21569 -0.37936 0.27377 -0.24892 -0.038522 -0.29133 -0.64109 -0.55138 -0.24495 0.65093 -0.0069848 0.41873 0.050112 -0.22116 0.28887 0.82337 0.20455 -0.22908 -0.54315 0.35053 -0.33815 -0.50246 0.22672 0.18738 0.185 -0.11623 0.038812 0.0076612 0.54322 0.023975 -0.58162 -0.50594 -0.08665 0.37579 0.33068 0.29172 -0.37791 -1.2169 0.50939 -0.064147 0.24145 -0.67614 0.18667 -0.0092105 0.085232 -0.4932 0.41986 0.43313 0.59024 0.12591 -0.084607 0.37461 -0.21939 -1.1322 0.76249 0.4928 0.25288 -0.052133 -0.39413 0.09449 0.51004"
chicago_42b_300 = "0.46441 0.17556 0.23809 0.45602 -0.15059 0.13759 -1.3554 -0.6271 -0.024367 0.01475 -0.010201 -0.28774 -0.076792 -0.31125 0.47816 -0.22781 0.079248 0.23297 0.18741 -0.22383 -0.61861 0.19305 -0.4599 0.24142 -0.39694 0.17871 -0.40394 0.17748 0.37744 -0.48943 -0.026469 0.60689 -0.1361 -0.012463 -0.15513 -0.27336 -0.22729 0.24301 -0.23009 0.45281 0.60101 0.27274 0.73229 -0.097865 0.15079 0.10704 0.58168 0.029993 -0.34754 0.43338 0.053771 0.38705 -0.023537 -0.23083 0.33769 0.40793 0.1842 -0.29798 -0.34518 0.32571 -0.44238 0.18726 -0.021894 -0.12413 0.11937 -0.33239 -0.36455 -0.1491 0.41013 -0.29135 0.010105 0.27892 0.29462 -0.30876 -0.65199 0.023873 -0.065043 -0.38034 0.67232 -0.18202 0.68676 -0.37514 -0.33257 -0.13587 0.36592 -0.14234 -0.16603 -0.12717 -0.17903 0.0064902 0.1119 0.24826 0.20662 0.035493 -0.067014 -0.02554 -2.1356 0.084944 0.36144 -0.16441 0.21296 -0.26081 -0.10458 -0.44568 0.13793 -0.025359 0.28367 0.042743 0.15688 0.14663 -0.15407 0.11664 -0.43685 0.0070799 -0.18188 0.62478 0.31177 0.096832 0.048117 0.23482 -0.2764 -0.38421 -0.2211 0.27965 -0.1147 0.64666 0.06854 -0.23105 0.087375 -0.61242 0.38381 -0.77439 0.082016 -0.042461 0.74764 0.026419 0.27101 0.52077 0.3596 0.5305 -0.028377 0.44302 -0.17175 -0.38954 -0.06011 0.22585 0.10154 0.25063 -0.59718 -0.034298 -0.30725 -0.30825 0.19943 0.36792 0.22865 -0.25858 0.44481 0.24063 -0.55466 -0.02919 0.053714 0.35481 -0.42923 0.29688 0.12065 0.22598 0.27443 -0.15789 0.11308 -0.32637 0.3979 -0.48298 0.13673 0.34167 0.072549 -0.38864 -0.11506 -0.22409 -0.06057 -0.11853 -0.31417 -0.25346 -0.097883 -0.18846 -0.38807 -0.34982 0.29011 0.16468 -0.038046 0.070089 0.41487 -0.062529 0.56335 -0.24273 -0.36571 -0.60352 -0.99862 0.17812 0.30394 0.6503 0.18476 0.30434 -0.1884 0.023957 -0.12558 0.0038385 -0.18349 0.32322 0.17122 0.34691 0.40847 -0.35098 -0.12004 -0.40178 0.015303 -0.53893 -0.21822 0.020231 0.082771 0.0092712 0.065352 0.23777 0.37846 0.34885 -3.5408 0.36354 -0.066381 0.37034 0.51532 -0.20764 -0.078374 0.24464 -0.51483 0.23848 0.2311 0.24328 -0.0032775 0.11885 -0.21495 -0.20859 -0.1138 0.34236 -0.24131 0.60351 0.26972 0.054094 0.015131 -0.48307 0.12872 -0.18952 -0.56354 0.6413 0.30545 0.097306 -0.19803 -0.20786 0.10561 0.073559 0.44097 -0.54384 0.32488 0.21128 -0.27894 -0.11474 0.35741 0.59446 0.16221 0.019925 0.16199 -0.080103 0.22039 0.16038 0.1624 0.58758 0.13204 0.20358 0.079208 -0.51715 -0.26823 0.01164 0.13237 0.50107 -0.49233 0.26579 0.26139 0.29203 -0.12109 -0.31538 0.14063 0.23246 -0.27846 -0.59498 0.012895 -0.025799 0.12705 -0.18381 0.39116 0.21832 0.056371 -0.70294"
chicago_deps_words = "-0.000584603931361 -0.00762492663376 -0.0657422931289 0.0413295476285 0.0577379557575 0.0589905848148 -0.0201654758392 0.028798504178 -0.115368234256 -0.0315931961426 0.0336952791321 0.0289859970004 0.0367795688389 0.0896731951871 -0.0672997619149 0.0518987999216 0.0564061667061 0.0617679041927 -0.00516457501683 0.0749632032456 0.0150081120848 0.0279021770402 0.0439523165418 -0.0431343299364 0.0783651162827 -0.0943021700784 0.0321796028895 -0.0233074556453 -0.0883423894897 0.0800315734663 0.054790024467 -0.0398387830197 0.0249434288561 0.0822777178115 -0.011464596077 0.00539009085915 0.0730758192048 0.0272279240058 0.0230006492086 0.0455112603587 -0.0314522487411 -0.0201015578316 0.00206684613916 -0.0688795200574 -0.000691625621066 -0.0354923585006 -0.0186971644793 0.0290913797669 0.0294680043349 -0.019137215378 -0.0064199902437 0.0526733550603 -0.0300704725299 -0.0711217309868 0.0502628267109 -0.00216534542785 0.0302661599687 -0.0400952745119 -0.0087316915198 -0.0798476862751 -0.0572139919872 -0.0455633781188 0.000129311046214 -0.0316390859942 -0.0669837775079 0.0730745080662 0.0390625889578 -0.077724297283 0.0570319076116 0.0245069835885 -0.000699656345102 -0.0975669052376 -0.00705261462695 0.0389065634622 0.0200781212288 -0.10703398163 0.000726698579101 0.0390407912782 0.100275389838 0.0652878197054 0.104542818255 -0.085820086573 -0.0225324088296 0.139087223535 -0.0221570954002 -0.0396412927653 -0.0787084707083 0.0142378181467 0.100976521214 -0.0254269112215 -0.00399438380015 -0.0623030126412 -0.0108306605551 -0.111486936162 0.0554601801931 0.0359737102658 -0.0664349021039 0.0169195882977 0.00927761686192 0.0672945173604 -0.0163764491252 -0.0470782348997 -0.00160286696067 -0.0539353259803 -0.0662693708534 0.00340125746777 -0.0225245419979 0.0736512451658 0.0148697869606 0.0162302571692 0.0596038699034 0.00233776015613 0.110685011004 -0.0307394810098 0.0417351811385 0.114826734007 0.00222205217308 0.0209067608355 -0.0332511309252 0.152155669927 0.00741793062443 0.0288624221857 0.00336241498621 0.044810784552 0.0710730549656 0.0696773479066 0.0365750312145 0.093872772181 0.0240928276775 -0.0282594623136 0.00379246845296 0.104366797896 0.0104633778497 0.018811725216 0.00240446433333 0.169678545881 0.0400454512444 -0.00730484491861 0.0178940920757 -0.0498814492653 0.171774564854 -0.0237512760675 -0.00629477650567 -0.0205819262428 0.0109439101532 0.0726400295066 -0.0185488419231 -0.0523921158267 0.0259080990943 -0.0548244418557 -0.0548403394114 -0.0022540111769 0.0397438893622 -0.0334478017179 -0.032004074207 0.00854272366646 -0.0773645536247 -0.00861778635235 -0.0557684616607 0.0496264328041 -0.0469741632719 -0.0836029511698 0.00831163548501 0.0667102412137 -0.0946874809398 -0.0527485816385 -0.0255785116242 -0.0304395580509 0.0181791008328 -0.124870547499 -0.0760950436577 0.119649265737 -0.0290795795193 0.0650218224582 -0.00187935331677 0.0479255582317 -0.0795543190093 0.079013310437 -0.0453830965588 0.044486769421 0.0197146080469 -0.00970619529773 -0.0546476020346 -0.0100110350264 -0.0355443123683 0.095683126828 -0.035985838298 -0.0168592759213 -0.0343692043818 -0.0345683335595 0.0296600861425 -0.00172103332863 -0.0255249188332 0.0105118899786 -0.134087196415 -0.0575325986714 -0.00194130461648 -0.0581437531598 0.0485068843165 -0.0716799482534 -0.0146124760068 0.0293106677007 0.0533962841159 0.0074682455689 0.0919939105412 0.0780937105887 0.0322012366767 0.0574308215362 0.0289150316227 0.0589484644867 -0.00896064910099 -0.0970509721913 0.00541631363152 0.0177587170133 -0.071998227153 0.0410832174606 0.0836670330697 -0.0626262083106 0.0524622617428 0.00145208601958 -0.0180443813398 0.0668351271671 0.0135199697532 0.0176239975203 0.0323139945979 0.019612994804 -0.0254793567662 0.0147811212115 0.0981531480922 0.0790905037231 0.0413180751656 0.000682939327721 0.0959499435368 -0.0622322111558 -0.0832607439904 0.0276458494404 0.0713292186731 0.147698454194 0.0696158882838 0.00297054843171 0.0235613248602 -0.0107906708273 0.0317369297136 0.0526530324117 0.06295645135 -0.101321514563 -0.104726049877 0.00507197585193 0.0602927093549 -0.0394572416818 0.0253838075394 0.0621022445403 0.0756295894482 0.00633574958748 -0.0159265646868 -0.0477965749701 -0.0541449442668 0.0249131087755 -0.00466060611049 -0.027583570356 0.0457534932184 0.0150192567631 0.00127704901406 0.0756266393864 -0.00070817874612 0.197414372209 0.0467448779061 -0.03886837655 -0.086875717053 -0.0589678037813 0.0730915528682 -0.0594355524833 -0.0557210967782 -0.0121159041855 -0.098762991442 0.106133393291 0.00307363670556 -0.0635407274967 -0.0405699066916 0.0162477936483 0.0160260473295 -0.0176218669201 -0.0404305982135 0.00536927653359 0.0768122364818 -0.0198685029422 0.0348241694823 0.150694897614 0.0390632445271 0.0790044602513 -0.064172368526 -0.0257519097065 -0.0428434210555 -0.00482023723725 0.0533692418819 -0.0293103399161 -0.0793037276409 0.0685176457988 0.0924526451652 0.00760657069311"
jack_deps_words = "-0.0646929099681 0.0295205553827 -0.00185041936563 -0.0268651457157 -0.00492767173157 0.0666390748934 -0.050571845508 -0.0510196503017 -0.0265582307611 0.0321012206749 6.89566466011e-05 -0.104659818538 0.0174614104105 0.0889038035624 0.0306324606387 -0.0159645385519 -0.00590645924052 -0.104333721399 0.0101339812318 0.0243694773452 -0.0369644005787 0.0195109276239 -0.123666883087 0.0178065243709 0.0205036056804 -0.0013492021094 0.0485193517487 0.0318511908196 -0.0656584683841 -0.066897703659 0.0937380448256 -0.0592638556166 0.048970298452 0.0357595609453 0.0558104009221 0.0779750845763 0.0824162564175 0.0157748664329 0.0628575386956 0.0352805024196 -0.0366359883481 0.0709334038036 0.0412466579417 0.0567547927896 -0.0112827625841 -0.0226280326321 -0.0183042689902 -0.049431166975 0.0322748525189 0.0241488822215 -0.0484110385508 -0.0696756477987 -0.00357532771262 -0.114714590576 0.0503166893792 -0.0552332817455 -0.00853838726762 0.005576558737 0.0645065451222 -0.00405091360141 0.0719513825002 0.0829710514998 -0.0713592152305 -0.0523729865027 -0.019191941122 -0.0934033487759 0.024192042137 -0.0501903515423 0.0164960173581 -0.0114618514289 0.0514691087321 -0.0753044614526 -0.0403325276242 -0.0117234567405 0.051233630879 -0.0436862680312 0.0414652687015 -0.000553637536739 0.0297494186894 0.0276848533829 0.0467248253005 -0.057826018585 -0.0247040080312 0.0744604453273 -0.0287952703659 -0.0553406027614 -0.105728233151 -0.0554050945892 -0.0308905933133 -0.029739827597 -0.00578227113117 -0.0539272395516 -0.0255710097054 -0.000737356564015 0.0604134637873 -0.0890440319469 -0.0551340635489 0.0579439228752 0.0585837148793 0.00223753569582 -0.0322612926987 -0.0302823857685 0.00673608872732 -0.0901541182026 0.00652921878752 0.0458568314443 0.00953420723365 0.0663897064927 -0.0187639799676 -0.0862136675267 0.0404398486401 -0.00213848286294 0.114407179531 0.112034541724 0.0252841037537 -0.0406321665778 0.0338276172948 0.0804700914922 -0.0907899414788 0.0429019481875 0.018013725038 0.0139919154409 0.0323701019875 0.0495222823522 -0.0433092388843 -0.0166853587499 -0.00174276762237 0.00498290319432 -0.0717112744646 0.0134655629082 -0.0202605210988 0.0246945823026 -0.0192369200378 -0.0300530263708 -0.0412258221205 -0.0596982659538 -0.0342132453521 -0.0133212004322 0.0193700377848 0.0283279526602 0.114042221931 -0.120912916678 -0.0301689462971 -0.00681992810341 0.0113677595059 0.0505867282375 0.0907930833884 -0.00192169110348 0.0200584467052 0.00107916325112 0.0479273498426 -0.0352128686823 0.0299270192612 -0.0122959457346 -0.0813336205295 -0.020581822692 0.0312034613598 -0.070569438386 -0.0282298920092 0.111216653057 -0.0345036239406 0.0274463989838 -0.0650461267478 -0.00573381957853 -0.186289109293 0.00886630340722 0.0116922030086 0.0738722467854 0.0240537981165 -0.0624193249942 -0.0545964662873 0.12970083771 0.0244610888134 -0.0124350165734 0.080830584273 0.0172634701084 -0.00810976465854 0.119516751289 0.0983677312402 0.00158600287182 0.0363431293047 -0.0118825365823 -0.00162767451437 -0.0245827964678 0.0993451958399 0.0370447673179 -0.0811895887808 -0.0668381727411 -0.0630882210025 0.0185392507524 -0.0314880522202 0.0733824396218 0.0507214996211 -0.00386702921047 -0.0943975151053 -0.0472753209277 0.00549635736145 0.0850705085388 -0.0178336440112 -0.0150213042301 -0.0240369310231 -0.0342906355454 -0.0342775718162 0.112538074071 0.133159749405 0.0114170378768 0.0256196266217 0.00186712109538 0.0500115934248 0.159046107612 0.072561574409 0.0476735166231 0.100066181401 0.0170132748895 -0.0342312699911 -0.0324453424533 0.056626305225 -0.034475181391 -0.058446793768 -0.0507487846252 -0.0876883806547 0.0852585270213 0.0739843633475 -0.0451985187102 0.0162102689521 0.0285688875141 -0.035068175479 0.0164050673446 0.0196260207319 0.126323119572 -0.0107440077769 0.0114302669697 -0.122161246954 0.0466535535626 0.122523724099 0.026148128882 -0.00319730638377 0.137150966725 -0.0740959838186 0.0687636672088 0.05563098135 0.0355207758189 -0.0314118195725 -0.00277000668397 0.097932824812 -0.0953004006939 -0.0398744702835 0.0123181044651 0.0339637115878 -0.115681967993 -0.0339642076787 0.0257674617346 0.0633819068643 0.0427599008028 0.0205796729644 -0.0238986870026 -0.140358194929 -0.0351131543948 0.0347758125265 -0.0335334353421 0.0124856178536 0.0339352690381 -0.0156343073211 0.025592176254 0.0301252902906 0.0898157841524 0.020322863199 0.0401871729663 -0.0326297229352 0.00939596321312 0.122684292214 -0.00251237010026 -0.0579452457845 -0.107438424132 -0.105158059248 0.0756500715039 0.0300240877302 -0.0825024108848 0.0134893752754 -0.016028865016 0.00138111729595 -0.0930122637179 -0.00227375033756 0.0934273265067 0.0903112136805 -0.0228342411173 0.0181511422402 0.057201770765 0.03460929132 -0.0434246627196 -0.0160812852965 0.0759687272784 -0.0186751796816 -0.115066153719 -0.0217476365014 -0.0788501890699 -0.0960182443459 -0.0176434758012 0.019116369929 0.0186450834954"
jack_42B_300d ="-0.28698 -0.21722 0.30845 0.30496 0.22069 -0.33922 -1.9691 -0.38099 0.054915 -1.0485 0.67262 -0.25503 0.1906 0.16262 0.00020125 0.055854 0.02745 0.054704 0.21116 0.2462 0.17712 0.29696 0.37754 0.24502 0.43622 0.053589 0.094141 0.009194 -0.24878 0.0089394 0.93134 0.16228 -0.28208 -0.28112 -0.40543 0.20494 -0.12323 0.60589 -0.51968 0.72584 -0.10705 0.43901 -0.26305 -0.23328 -0.51501 -0.35024 -0.51796 -0.10207 0.38194 -0.028124 -0.08924 -0.67798 0.049834 -0.55225 0.13212 -0.3269 0.32765 0.20063 0.78249 0.28372 -0.15793 0.6594 -0.13717 -0.4323 0.30147 0.0019712 0.048771 -0.20242 -0.36946 -0.26551 0.42951 0.063166 -0.33356 -0.19256 -0.36422 0.11466 -0.069216 -0.45202 0.0042593 -0.16733 -0.15375 -0.83996 -0.028537 0.35788 -0.23357 -0.094234 -0.046104 -0.23499 0.0015028 -0.035846 -0.13185 -0.07531 -0.10267 -0.10545 -0.087627 -0.2742 -1.1762 0.20805 0.12185 -0.18202 -0.46454 -0.29087 0.35625 0.52132 -0.83992 0.048193 0.081325 -0.3322 -0.19695 -0.10822 -0.20875 -0.29148 0.054031 -0.30322 -0.08124 -0.047395 -0.17315 0.50489 -0.089788 0.19362 -0.36896 0.14411 0.093233 -0.076574 -0.59287 -0.071608 -0.15096 0.060248 -0.015083 -0.018893 0.23609 0.010496 -0.10884 -0.0517 -0.12431 0.29227 -0.21013 -0.13922 0.072419 0.58688 -0.61001 -0.5626 0.9334 0.25525 -0.49944 -0.29248 -0.042154 0.40284 0.054493 -0.21118 0.046976 0.10876 -0.31401 0.022975 0.19264 -0.085935 0.2163 0.096272 0.034231 0.0075131 -0.59517 -0.11798 -0.53958 -0.50203 -0.44099 0.096243 -0.53942 -0.21259 -0.066789 -0.01428 0.41055 -0.46386 0.12299 -0.37763 -0.30867 -0.35821 -0.31359 -0.43299 0.36275 -0.063867 0.35763 -0.16676 0.094479 -0.069914 -0.036027 0.059374 -0.018414 -0.84684 0.099897 -0.29792 0.029891 -0.36891 0.69179 0.0079999 -0.12125 0.1291 -0.029203 0.15736 -0.19491 -0.22073 0.38858 -0.37634 -0.3086 0.45019 -0.016162 -0.045069 -0.032985 -0.063159 0.18979 -0.019892 0.20999 -0.37225 0.1232 -0.36331 -0.0064289 0.17893 0.21961 0.23844 -0.053673 0.23443 -0.22852 0.3085 0.030144 0.17927 -3.3485 -0.50669 0.083775 0.53322 -0.23532 0.3746 0.13642 0.23018 0.25864 0.17659 0.0072182 0.072797 -0.011113 0.45269 0.23069 -0.34848 -0.012536 -0.26572 -0.20051 0.1959 -0.0017407 0.03258 0.14413 0.51685 -0.20787 0.45376 0.19481 0.015435 -0.44741 0.20011 0.021346 0.23814 -0.4649 0.73146 0.20792 0.31486 0.22515 0.057602 0.074526 0.30899 0.091287 0.35952 0.28694 0.46709 -0.43715 0.43717 0.16724 -0.014046 -0.35041 -0.18229 -0.13595 -0.20824 -0.23539 0.12526 0.35831 -0.2889 -0.32711 -0.594 -0.0096619 0.28084 -0.24352 -0.19794 -0.19789 -0.039853 -0.14256 -0.31122 -0.063725 -0.27758 0.51818 0.019343 0.40109 -0.27427 -0.17261 -0.15285 0.42624 0.2783"
jack_6b_300d = "0.15066 -0.10613 0.5949 -0.10453 -0.221 0.53244 -0.38249 0.20305 -0.10078 -0.4929 0.6288 -0.62772 0.159 -0.46485 -0.097863 0.223 -0.16687 0.15571 0.058579 0.31217 0.45905 0.12908 0.076218 0.24813 0.33306 -0.2923 -0.19074 -0.13186 0.12979 -0.32847 -0.80823 0.071951 -0.60185 0.10012 -1.2027 0.1986 0.51295 0.21587 0.22548 0.090291 -0.28488 0.22709 -0.0076812 0.18051 -0.068706 0.09517 -0.12487 0.094389 -0.20476 -0.068432 -0.58054 -0.26996 -0.698 0.28967 0.0039802 0.11612 -0.61512 0.59156 -0.34977 -0.45648 0.079135 -0.15626 0.38985 0.62796 -0.025925 -0.91835 0.21697 -0.28113 0.0084693 0.024773 -0.51109 -0.34708 0.19057 0.66394 -0.60694 0.2012 0.17724 0.2833 -0.024985 -0.2109 0.16179 0.18675 0.29666 -0.12493 -0.22109 -0.78169 -0.17771 0.042472 0.39549 -0.59354 0.15461 0.67936 -0.33085 -0.11666 0.082801 0.041013 0.17323 -0.22059 0.28447 -1.1497 -0.21089 0.61815 -0.16742 -0.13285 0.15985 0.12422 -0.20261 0.0080897 0.12973 -0.20101 0.16102 0.54883 -0.1852 0.072104 -0.10978 0.20404 -0.16611 0.055742 -0.089351 -0.022771 -0.29419 -0.024907 -0.33351 0.20124 0.17303 0.14531 0.32799 -0.015825 -0.37111 0.10032 -0.26452 0.18049 -0.016737 0.032639 -0.14829 -0.15003 0.17901 0.45985 -0.47375 -0.073631 0.74916 -0.4161 0.31175 0.1238 -0.65532 -0.39468 0.2012 -0.41013 -0.27628 -0.17573 0.48481 0.78353 0.41721 -0.15213 0.37763 -0.32791 0.33157 -0.4604 0.032014 0.14408 0.43071 -0.25455 -0.21666 -0.31961 -0.48817 0.3631 -0.31387 -0.20191 -0.33539 0.19679 0.12998 -0.11259 -0.45961 0.28014 0.34159 -0.25609 -0.31513 -0.55271 0.082628 0.32148 -0.0379 1.1269 0.089414 -0.23314 -0.13392 -0.061194 -0.29925 -0.17982 0.25079 -0.30837 -0.2122 0.11067 0.48385 -0.031396 -0.58965 0.099345 0.10626 -0.26161 0.21009 -0.37123 1.0973 0.20727 0.55106 -0.31125 -0.037127 -0.51174 0.58478 0.61216 0.018298 -0.53849 0.32509 0.037555 0.42248 -0.21392 0.44503 0.45873 -0.026984 0.48324 -0.10463 -0.59655 -0.10897 -0.24937 -0.25108 -0.38505 0.13008 -0.21081 0.37056 -0.30593 0.068949 -0.41011 0.26985 -0.044301 -0.11991 0.20107 -0.10195 -0.048204 -0.073743 0.089076 -0.34337 0.10474 0.093117 -0.20925 -0.19767 -0.22888 0.0099675 -0.1404 -0.69567 -0.19522 -0.15009 -0.37715 -0.071349 0.23601 -0.25901 -0.21652 1.0154 0.015187 0.4586 -0.079744 0.27355 -0.47655 -0.63104 -0.38203 0.48645 0.35842 -0.37212 -0.41254 0.1469 -0.22853 -0.53466 0.22462 -0.31023 0.14383 -0.26615 -0.46913 -0.33118 -0.00023755 -0.28416 0.21133 0.03655 -0.26031 0.07449 0.04944 0.14128 -0.36683 -0.41503 0.29501 -0.095817 -0.12307 -0.2674 -0.34101 -0.023343 -0.063886 0.38951 -0.28875 -0.46129 0.32275 0.21675 0.1063 -0.4935 0.12187"
happiness_deps = "0.0966383694537 0.114730820251 0.0943865320455 -0.0305883568227 -0.0118784162374 -0.0377270605978 0.112947579318 -0.00280549092829 -0.0102715512615 -0.0552985587424 0.000198814317753 -0.0283996599196 -0.113057857776 -0.0193403019918 -0.0602950078041 -0.0186125337455 -0.0553764842143 0.000671585372566 0.0660557526769 0.0411062082364 -0.0531517815686 0.0350217595619 -0.0380038003874 -0.00515769216973 0.065013151609 0.0924437874129 -0.0112661446726 -0.00927660996883 -0.065754139355 0.0852716870071 0.0348161615535 -0.0490622597622 0.0637266855599 0.0422604792886 0.0801773092833 -0.00419823479727 -0.0670513897327 -0.119151699253 -0.0350302826604 0.00659844369549 -0.049375353176 0.049234287199 0.00634709926053 -0.0394109813416 -0.0627406152473 -0.0328436730467 -0.0259121327471 -0.0641424040371 -0.00866172929232 -0.0851668007135 -0.0608964950401 -0.0240968867103 -0.100075787255 0.0238116238222 0.00489069306408 0.0720052233019 0.0225757745416 -0.111561097318 -0.0450779721311 0.011297454014 -0.0715623700622 0.0625783284945 -0.0577521674618 -0.125795193612 0.0205248387406 -0.0238935499321 0.101882336253 -0.0281429233203 0.0997077285535 0.0829534042188 0.0015047617348 0.0425426112425 -0.0269046388688 0.06646834022 0.0869293426923 0.0286035185201 -0.0937071193375 -0.0957832765525 -0.0238140589932 -0.0577013767524 -0.038372206971 -0.0313552617457 -0.0680644208671 0.0751575521564 -0.0688031473829 0.0458229605151 -0.0499123083807 0.00631961661643 -0.0286770954724 0.059837021716 -0.00639615056203 -0.00910319100576 0.0562033987083 -0.0168301625171 0.0480382703584 -0.00716409912972 -0.0675379021096 0.0898898148604 0.0648675631716 -0.0263381137306 -0.0243024847187 -0.0404198378971 0.00701711916603 -0.0556424396752 0.00746919126738 0.0319670114881 0.0131610555892 0.00390584033695 -0.139080268981 -0.0967947422198 0.0807201784746 -0.0085664097419 0.0998922797268 -0.0566288578695 0.0155797022107 0.0218760107618 0.140680176326 0.0345599467766 -0.0668593591056 0.0909884248612 0.110114605746 0.0433860501111 0.0737863769448 0.00190969588329 -0.0528644313911 0.0688807249732 0.0610413877144 0.0670108615297 0.0227841556026 -0.0109774029688 -0.061034430083 0.00949647112162 -0.052552381622 0.0461972810853 0.0674989393737 -0.0705910847163 0.00239012033267 0.000242647395682 -0.0133417800652 -0.0942287677531 0.0193857005368 0.00123115287931 -0.0670922658173 -0.104392127846 -0.0236846470488 0.0981187794785 0.0189604153164 0.0219725478978 -0.039518476747 0.0286678766107 -0.0675439900371 -0.112058394023 -0.0344079225301 -0.0421275885285 0.0601786414186 0.0288574720669 0.0278630525965 -0.0597624011191 0.00924043028546 -0.095623946793 0.0352880629044 -0.0516318869855 0.0111007269857 0.0480212241614 -0.027678675364 -0.103537034945 0.0567984501353 -0.0200468494622 -0.0511371993917 -0.0770886427563 -0.141236438958 0.0185048643993 -0.0410234124226 0.00468161623999 0.00451567673069 -0.0147919243934 0.0262821047977 -7.49684785226e-05 0.0220977852633 -0.031151577086 -0.0155534371521 -0.0337050278162 -0.025944659674 -0.0308148277254 0.0100763897003 0.0492403751265 0.0499665779057 -0.0711602189663 0.0300663605256 0.0215949224526 -0.0782863990048 0.00845473975765 0.00221583166566 -0.0833192016906 -0.0783058803728 0.0357997966951 0.0689617813792 0.0756117115471 -0.00462525942551 -0.0803456839636 -0.0031074521318 0.0625485846202 0.0392203422407 0.000480946271729 0.0505663257339 -0.0180437473771 -0.0566215523565 0.0331513742961 0.0991078067845 -0.00594286087518 0.0114753954375 -0.0738065540759 0.00542225610437 -0.00308779682305 0.0418852890144 -0.00190186854795 0.0571922520735 0.00160408192328 0.0525664708256 -0.0948876554483 -0.041695867499 0.0278743587476 0.0492682056522 -0.129083544161 0.120817356215 -0.0535678479274 -0.0788322251895 -0.0141994820782 -0.00249013628429 0.0226223906721 0.0484183309746 -0.0503200255817 0.107551936154 -0.0256101715436 -0.0625423227519 0.0126919372909 0.123828619092 -0.0280423855463 -0.0719838285853 0.182559029531 -0.077194224813 -0.0195205046455 0.0289606189526 -0.0269175104869 0.00384235195027 -0.0291683042504 -0.0392292132208 0.00426328865102 0.0397164213608 -0.0792954295011 -0.0243887593482 0.0639079318583 0.0712866739173 -0.0347184068321 0.0771053410717 -0.0833256374996 -0.0189503267508 0.00839473018668 0.0782331731244 -0.0142276604855 0.0370641722645 -0.0891656993706 -0.0401563176072 0.118429497112 0.0400568234779 0.101042550141 0.00906266280275 -0.0342285895803 -0.0110184529942 -0.127268646006 0.029410255883 -0.0281312692877 -0.0758583595809 0.0309818108794 0.0109086963586 -0.000976329628648 -0.0431303571565 -0.0618794344186 -0.0133795252157 0.0329273385645 -0.0709102660576 -0.0239394702995 0.0709939315754 0.00311388794086 0.0603442330464 -0.0249225836187 0.00872295644879 0.00848831032924 0.0422615229333 -0.120903109022 0.00153746260246 -0.0189520661587 -0.018325183568 -0.0370074675684 0.039890536087 -0.0262236606938 -0.0215568294206 0.0464783693946 -0.0617578498096 -0.00480111355958"
happiness_6b_300d = "-0.36122 0.31083 0.16319 0.217 -0.18337 0.25231 0.21821 0.11136 -0.014099 -0.91588 0.13674 -0.38058 -0.50144 0.36518 -0.076403 0.081589 0.51216 -0.045155 0.18487 0.36205 0.171 0.4252 -0.48401 -0.22759 0.0064638 0.60065 0.25588 0.16524 0.90668 -0.00038606 0.015971 0.23889 -0.19654 -0.27445 -0.42196 0.55593 -0.78969 0.13143 -0.17582 -0.38865 0.067548 -0.26193 -0.10242 -0.48114 0.45214 -0.46552 0.2561 0.43706 -0.16241 -0.11267 0.64985 0.25626 0.39585 -0.49016 0.36559 0.60171 0.48122 0.0026481 0.12532 0.30321 -0.014775 0.03279 0.16155 0.068649 -0.20968 -0.19526 -0.33259 0.33793 0.16306 0.38969 -0.024987 -0.21581 -0.24125 0.10408 -0.0034862 0.61561 0.037081 -0.15371 0.06414 0.57098 0.06054 0.56689 0.2941 0.13521 -0.031336 0.22634 0.36165 -0.1323 -0.10528 -0.47299 -0.0088071 -0.2934 -0.46633 -0.41103 -0.042537 -0.011202 -0.075189 0.25193 -0.11309 -0.047335 0.38954 0.077607 -0.038676 0.1214 0.013658 0.22141 0.24952 -0.75912 0.19555 -0.031098 -0.026453 0.17901 0.33421 -0.47259 0.27176 0.58683 0.65734 0.33737 0.35846 -0.29651 -0.23919 0.12452 0.36385 0.51739 -0.082814 -0.68295 0.76122 0.62901 -0.82813 0.59955 0.12072 -0.15481 0.16941 0.07657 -0.20247 -0.33084 -0.61257 0.0011643 -0.011203 -0.4553 -0.32858 0.24714 -0.015428 -0.1879 0.47527 -0.70693 -0.32279 0.54255 -0.50566 0.33536 -0.81531 0.031431 -0.11727 0.82971 -0.1336 0.27612 -0.12614 0.43088 -0.29797 -0.26053 0.75228 -0.57519 0.48674 0.19512 0.5549 0.29528 0.016752 0.20652 -0.35915 0.25869 -0.098863 -0.62515 -0.42219 0.37579 -0.22966 0.0034914 -0.41548 -0.24856 -0.059461 0.12135 0.1745 -0.30038 -0.26301 0.14345 -0.035052 0.22837 0.188 -0.38415 -0.27365 0.38571 0.11131 -0.55738 -0.094698 -0.10905 -1.1059 0.29079 -0.015723 -0.22755 0.11298 0.25291 0.45035 0.34179 0.3682 0.36266 0.20011 -0.26366 0.3728 0.3596 -0.46296 -0.17429 -0.31148 0.062398 -0.3371 0.18813 0.45989 0.48221 -0.02291 0.32096 0.77378 0.30922 -0.18925 0.35438 -0.44228 0.36023 -0.247 -0.040147 0.2007 0.48619 0.35419 0.070303 -0.072055 -0.23751 0.19165 -0.56734 -0.73552 0.62871 -0.25455 0.42548 -0.20956 0.041393 -0.35728 0.43184 -0.02542 0.040245 -0.38369 -0.45885 0.11833 -0.082805 0.24612 0.0020692 -0.18029 -0.30307 0.32744 -0.18955 -0.54514 0.33921 0.15913 0.0015398 -0.18268 -0.092756 0.3118 -1.2686 0.56676 -0.46927 -0.40257 0.68172 0.1655 -0.24211 0.1526 -0.011781 0.066103 -0.73158 0.59462 -0.090463 -0.17501 -0.52251 -0.79004 -0.53364 0.584 -0.42745 -0.37637 -0.0081708 -0.59185 0.32908 -0.018555 0.27352 0.098062 -0.082735 0.60912 -0.07091 -0.45953 -0.021167 -0.072218 -0.10957 0.042012 -0.24771 0.16179 0.70207 0.10804 -0.078332"
happiness_42b_300d = "-0.1256 0.11981 0.076408 0.15257 -0.56863 -0.28309 -2.9143 0.050805 -0.37773 -0.52046 -0.29189 -0.48314 -0.079542 -0.35126 -0.38832 0.47992 -0.034395 -0.4188 0.061326 -0.1101 0.10515 -0.47018 0.32833 0.56338 -0.59142 0.058326 -0.62812 0.43907 -0.19512 0.088062 0.35407 -0.036641 0.32375 0.14816 0.10635 -0.24916 0.16509 -0.42546 -0.142 -0.27692 0.17725 -0.4127 -0.16316 -0.21668 0.3173 -0.29823 -0.061766 -0.074035 0.20223 -0.40256 0.54729 0.0064492 0.10374 -0.066136 -0.097785 0.35405 -0.18263 -0.34184 0.38094 0.38161 -0.070472 -0.56352 0.36509 -0.059805 -0.077165 0.35472 -0.024285 -0.56305 -0.23648 0.79611 -0.091859 0.23833 -0.35187 0.018716 -0.1486 0.33218 0.59167 0.046439 0.51099 -0.43818 0.23114 -0.088303 0.14075 0.074717 0.35129 -0.1847 -0.29284 -0.27399 0.3651 0.20918 -0.37646 -0.16829 0.48476 0.74777 -0.18123 0.46147 -1.5746 0.18801 0.0010938 -0.27808 -0.28823 0.23707 0.26901 -0.5621 0.095475 -0.90376 -0.55691 -0.48064 0.41443 0.07036 -0.073282 0.3199 0.40843 0.050031 0.4685 1.1091 -0.95188 0.067162 0.4752 -0.076039 -0.28513 0.12544 -0.3606 0.31737 0.56375 0.30641 -0.39042 -0.26962 -0.065929 -0.1946 -0.48762 -0.22946 0.38027 -0.11517 0.0092299 0.2893 -0.047534 0.25884 -0.58068 0.084431 -0.37387 0.10336 0.1646 -0.38369 0.23526 -0.11294 0.11977 -0.052034 0.94369 0.61984 -0.014178 0.03588 0.28322 -0.29137 0.098019 0.31234 0.012438 0.28638 0.094164 -0.32222 0.3698 -0.23294 -0.76494 -0.064762 0.13432 0.33581 0.0033332 0.16351 0.47354 -0.13237 0.36545 0.31522 0.43337 -0.25889 -0.29424 0.13435 0.11398 -0.13917 -0.63611 0.30746 0.0045938 -0.20211 -0.12541 -0.35205 0.25428 -0.63335 -0.30942 -0.049636 0.34937 0.19955 0.12606 0.54241 -0.050811 -0.023005 0.21276 -0.28739 -0.037459 -0.11556 -0.30739 -0.092663 0.22248 -0.1307 0.17153 -0.21248 -0.22568 -0.18315 0.2728 0.08003 -0.59749 0.11248 -0.23534 0.0021515 0.41641 0.39554 0.048327 -0.28139 0.32753 -0.060091 -0.10993 0.62134 -0.11604 0.78099 0.73426 -0.33989 -1.0558 -0.33843 -0.35996 0.13266 0.10055 -0.4935 0.51432 0.3457 -0.2084 0.043694 -0.077613 0.021738 0.17343 -0.8085 -0.089205 -0.021837 0.43686 -0.27543 -0.58924 0.43458 -0.13806 0.3188 -0.10156 0.76325 0.80866 -0.16433 0.43269 -0.42737 -0.75185 -0.022824 -0.19112 0.19368 0.53949 0.66686 -0.32263 0.0047488 0.4729 -0.14648 -0.15987 0.5698 -0.17516 0.095304 0.10243 0.2079 -0.042051 0.29899 -0.67802 0.071892 -0.7551 -0.19825 -0.15131 0.19829 0.28444 -0.17552 0.11293 0.1342 0.28318 -0.10671 -0.32555 -0.18867 0.23742 0.57464 -0.20111 0.2578 0.098365 -0.30776 0.24025 0.30348 0.30444 -0.27881 0.45298 0.49753 -0.39747 -0.20815 0.41721 0.46173"

#compute Euclidian distance
def Eudistance(vector_1,vector_2):
	result = 0
	for index in range(0,len(vector_1)):
		val_1 = float(vector_1[index])
		val_2 = float(vector_2[index])
		val = abs(val_1 - val_2)
		val = val*val
		result = result + val
	result = math.sqrt(result)
	return result

#data normalization 
def Normalization(vector):
	result = []
	vector = vector.split(' ')
	for index in range(0,len(vector)):
		if vector[index] != ',':
			ans = float(vector[index])
			result.append(ans)
	mean = sum(result)/len(result)
	std = stats.stdev(result)

	for index in range(0,len(result)):
		result[index] = (result[index]- mean)/std
	return result 

# compute the original and normalized distance of word 'chicago' in different corpus
chicago_6b_300d_ori = chicago_6b_300d.split(' ')
chicago_42b_300_ori = chicago_42b_300.split(' ')
chicago_deps_words_ori = chicago_deps_words.split(' ')
# chicago_6b_300d_ = Normalization(chicago_6b_300d)
# chicago_42b_300_ = Normalization(chicago_42b_300)
# chicago_deps_words_ = Normalization(chicago_deps_words)

# compute the original and normalized distance of word 'jack' in different corpus
jack_deps_words_ori = jack_deps_words.split(' ')
jack_42B_300d_ori = jack_42B_300d.split(' ')
jack_6b_300d_ori = jack_6b_300d.split(' ')
# jack_deps_words_ = Normalization(jack_deps_words)
# jack_42B_300d_ = Normalization(jack_42B_300d)
# jack_6b_300d_ = Normalization(jack_6b_300d)

# compute the original and normalized distance of word 'happiness' in different corpus
happiness_deps_ori = happiness_deps.split(' ')
happiness_6b_300d_ori = happiness_6b_300d.split(' ')
happiness_42b_300d_ori = happiness_42b_300d.split(' ')
# happiness_deps_ = Normalization(happiness_deps)
# happiness_6b_300d_ = Normalization(happiness_6b_300d)
# happiness_42b_300d_  = Normalization(happiness_42b_300d)

# print the normalized distance of chicago
# dis_chicago_ = [] 
# dis_chicago_.append(Eudistance(chicago_6b_300d_,chicago_42b_300_))
# dis_chicago_.append(Eudistance(chicago_6b_300d_,chicago_deps_words_))
# dis_chicago_.append(Eudistance(chicago_deps_words_,chicago_42b_300_))
# print "Chicago nomralized distance in different wordvectors"
# print dis_chicago_
# print '------------------------------------'

# # print the normalized distance of jack
# dis_jack = []
# dis_jack.append(Eudistance(jack_6b_300d_,jack_42B_300d_))
# dis_jack.append(Eudistance(jack_6b_300d_,jack_deps_words_))
# dis_jack.append(Eudistance(jack_deps_words_,jack_42B_300d_))

# print "jack nomralized distance"
# print dis_jack
# print '------------------------------------'

# # print the nomalized distance of happiness
# happiness_ = []
# happiness_.append(Eudistance(happiness_42b_300d_,happiness_6b_300d_))
# happiness_.append(Eudistance(happiness_deps_,happiness_6b_300d_))
# happiness_.append(Eudistance(happiness_42b_300d_,happiness_deps_))
# print "happiness nomralized distance"
# print happiness_
# print '------------------------------------'

#print the original distance of chicago 
dis_chicago_ = [] 
dis_chicago_.append(Eudistance(chicago_6b_300d_ori,chicago_42b_300_ori))
dis_chicago_.append(Eudistance(chicago_6b_300d_ori,chicago_deps_words_ori))
dis_chicago_.append(Eudistance(chicago_deps_words_ori,chicago_42b_300_ori))
print "Chicago original distance in different wordvectors"
print dis_chicago_
print '------------------------------------'

#print the original distance of jack
dis_jack = []
dis_jack.append(Eudistance(jack_6b_300d_ori,jack_42B_300d_ori))
dis_jack.append(Eudistance(jack_6b_300d_ori,jack_deps_words_ori))
dis_jack.append(Eudistance(jack_deps_words_ori,jack_42B_300d_ori))

print "jack original distance"
print dis_jack
print '------------------------------------'

#print the original distance of happiness
happiness_ = []
happiness_.append(Eudistance(happiness_42b_300d_ori,happiness_6b_300d_ori))
happiness_.append(Eudistance(happiness_deps_ori,happiness_6b_300d_ori))
happiness_.append(Eudistance(happiness_42b_300d_ori,happiness_deps_ori))

print "happiness original distance"
print happiness_
print '------------------------------------'


# result:
# Chicago original distance in different wordvectors
# [9.1601025704556, 6.5899502761845685, 7.044946601840612]
# ------------------------------------
# jack original distance
# [8.993618266190921, 6.147560492077683, 6.683184602055798]
# ------------------------------------
# happiness original distance
# [9.66851737710083, 6.377412313071692, 7.1132643880976945]
# ------------------------------------
# [Finished in 0.3s]