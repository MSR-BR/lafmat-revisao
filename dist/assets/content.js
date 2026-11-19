window.siteContent = {
  // Add the supplied flyer here with its corresponding date and a description.
  weeklyBanner: {
    date: '2026-11-21',
    image: 'assets/johan-triana-2026-11-21.jpg',
    alt: {
      en: 'Flyer for Johan Triana’s seminar on light-driven chemistry and quantum technologies, November 21, 2026.',
      pt: 'Cartaz do seminário de Johan Triana sobre química induzida pela luz e tecnologias quânticas, em 21 de novembro de 2026.',
      es: 'Cartel del seminario de Johan Triana sobre química impulsada por luz y tecnologías cuánticas, el 21 de noviembre de 2026.'
    }
  },
  contact: {name: 'Luis De Los Santos Valladares, PhD', email: 'ld301@cam.ac.uk', phone: '+44 (0) 7512825533', tel: '+447512825533'},
  youtube: 'https://www.youtube.com/@Lafmatnetwork',
  facebook: 'https://www.facebook.com/61583070328062',
  conferences: [
    {year: 2023, url: 'conferences/2023/event-home/index.html'},
  ],
  // country code | name | affiliation | index of preserved biography (optional)
  members: `GB|Luis De Los Santos Valladares|University of Cambridge|0
BR|J. Albino Aguiar|Universidade Federal de Pernambuco|1
PE|Ángel G. Bustamante Domínguez|Universidad Nacional Mayor de San Marcos|4
BR|Isaias Gonzaga de Oliveira|Universidade Federal Rural do Rio de Janeiro|2
CO|David Landinez Tellez|Universidad Nacional de Colombia
CO|Jairo Roa Rojas|Universidad Nacional de Colombia|3
MX|Arturo I. Martínez Enríquez|CINVESTAV
VE|José Fermín|Universidad del Zulia
VE|Blanca Rojas de Gascue|Universidad del Oriente
CL|Felipe Mondaca Espinoza|Universidad San Sebastián, Puerto Montt|5
CL|Sergio Conejeros Espindola|Universidad Católica del Norte, Antofagasta
BR|Mario Reis|Universidade Federal Fluminense|7
BR|Augusto César Lima Moreira|Universidade Federal de Pernambuco|9
AR|A. D. Hernández Nieves|CONICET, Centro Atómico Bariloche, Instituto Balseiro|6
AR|Leandro Tosi|CONICET, CAB-CNEA, Instituto Balseiro
AR|Gabriela Grad|Universidad Nacional de Córdoba
BO|Gustavo García|Universidad Mayor de San Andrés
VE|Alexander Briceño|Instituto Venezolano de Investigaciones Científicas
CR|Sergio Paniagua Barrantes|LANOTEC, Centro Nacional de Alta Tecnología|10
MX|Alfredo Tlahuice Flores|Universidad Autónoma de Nuevo León|8
BO|Edgar Cárdenas|Universidad Mayor de San Andrés
CR|Tomás Rojas Solórzano|Universidad de Costa Rica
EC|Juan Ramón Primera Ferrer|Universidad Técnica de Manabí
SV|Carlos Rudamas|Universidad de El Salvador
GT|Lucía Nitsch Velásquez|Universidad de San Carlos de Guatemala`.split('\n').map(row => row.split('|')),
  collaborators: [
    ['Ximena Velásquez','Universidad Nacional de Colombia','CO'],
    ['Vanessa Parra','Universidad Nacional de Colombia','CO'],
    ['James Godoy Chepe','Universidad Nacional Mayor de San Marcos','PE'],
    ['Rodolfo Ccolque Rojas','Universidad Nacional Mayor de San Marcos','PE'],
  ],
  institutions: {
    AR:['Universidad Nacional de Córdoba','CONICET – Centro Atómico Bariloche (CAB-CNEA), Instituto Balseiro'],
    BO:['Universidad Mayor de San Andrés'],
    BR:['Universidade Federal de Pernambuco','Universidade Federal Rural do Rio de Janeiro','Universidade Federal Fluminense'],
    CL:['Universidad San Sebastián','Universidad Católica del Norte'],
    CO:['Universidad Nacional de Colombia'],
    CR:['Centro Nacional de Alta Tecnología (LANOTEC-CONARE)','Universidad de Costa Rica'],
    EC:['Universidad Técnica de Manabí'],
    GT:['Universidad de San Carlos'],
    SV:['Universidad de El Salvador'],
    MX:['CINVESTAV','Universidad Autónoma de Nuevo León'],
    PE:['Universidad Nacional Mayor de San Marcos'],
    VE:['Universidad del Zulia','Instituto Venezolano de Investigaciones Científicas (IVIC)'],
  },
  // date | speaker | title | affiliation | moderator | status | invited/recommended by
  seminars: `2026-11-14|Miguel Enrique Gámez López|Thermodynamic Fingerprints of Altermagnetism: From Magnon Splitting to Field-Induced Transitions|Universidad Nacional de Colombia (estudiante de Ovidio Almanza)|Eliana Vargas
2026-11-21|Johan Triana|Light-driven chemistry for applications in quantum technologies|Universidad Católica del Norte, Chile|Sergio Conejeros
2026-11-28|Debora Vasconcelos||DEFIS/UFRRJ, Brazil|Isaias Gonzaga de Oliveira
2026-12-05|Richard Caraballo|Investigation of caloric effects in polymeric systems via molecular dynamics simulations|Universidade Federal do Rio de Janeiro (UFRJ), Brazil|Mario Reis
2026-12-12|||||invited|Juan Primera
2026-12-19|Mercedes Cornelius|Decoding spatial-functional Dynamics in Complex systems|Cavendish Laboratory, University of Cambridge, UK
2026-12-26|||||christmas
2027-01-02|||||newYear
2027-01-09|Ismardo Bonalde||Instituto Venezolano de Investigaciones Científicas, Venezuela|José Fermín
2027-01-16|Deliang Zhang||Northeastern University, Shenyang, China
2027-01-23|Nestor Haberkhorn||Instituto Balseiro, Argentina|Leandro Tosi|pending
2027-01-30|Brian Cantor|Complexity in Multicomponent High-Entropy Cantor Alloys|University of Oxford, United Kingdom|Stuart Holmes
2027-02-06|Darwin Putungwan||University of the Philippines, Los Baños, Philippines
2027-02-13|Xiaoli Zhao||Northeastern University, China
2027-02-20|Pedro Grima||Universidad de Los Andes, Venezuela
2027-02-27|Rodrigo de Bragança|Non-Reciprocity Phenomena in Superconductor Open Nanotubes and Nanopetals|University of Antwerp, Belgium (previously Universidade Federal de Pernambuco)||recommended|Mihail Croitoru
2027-03-06|Paulo J. F. Cavalcanti|Helical phase in superconducting heterostructures
2027-03-13|A. Nikolaev|Magnetic Landau minibands in 2D structures|Moscow State University||recommended|Mihail Croitoru
2027-03-20|Nataliya Pugach|Static and Dynamic Inverse Proximity Effect in Superconductor–Ferromagnetic-Insulator Heterostructures|HSE University||proposed
2027-03-27|Mikhail Zhuravlev||Saint Petersburg State University||recommended|Mihail Croitoru
2027-04-03|Rafael Zadorosny||UNESP||invited|Isaias Gonzaga de Oliveira
2027-04-10|Durval Rodrigues||USP-Lorena, Brazil||invited|Isaias Gonzaga de Oliveira
2027-04-17|Fabiano Colato||UFSCar, Brazil||invited|Isaias Gonzaga de Oliveira
2027-04-24|||||mexico|Alfredo Tlahuice
2027-05-01|||||holiday
2027-05-08|Francisco Peña||Universidad San Sebastián, Chile|Felipe Mondaca
2027-05-15|José Solís||Universidad Nacional de Ingeniería, Peru|Arturo Martínez
2027-05-22|Pratap Kollu||Hyderabad University, India
2027-05-29|Graciela Díaz de Delgado||Vicepresidente de la Unión Internacional de Cristalografía||pending|Alexander Briceño
2027-06-05|||||invited|Felipe Mondaca
2027-06-12|||||invited|Felipe Mondaca
2027-06-19|||||centralAmerica|Carlos Rudamas
2027-06-26|||||reserved
2027-07-03|||||open`.split('\n').map(row => row.split('|')),
  // Add new editorial items here in descending date order.
  news: [],
  // Author records require an identity verified against the member's own profile.
  publications: [],
};
