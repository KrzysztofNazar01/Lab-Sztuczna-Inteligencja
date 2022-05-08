# Laboratorium 4

Algorytm genetyczny w problemach

optymalizacji dyskretnej

Problemami optymalizacji dyskretnej nazywamy problemy w których zmienne decyzyjne przyjmują war-

tości całkowitoliczbowe lub binarne. Do tej klasy problemów należy wiele praktycznych zagadnień m.in.

z dziedziny szeregowania zadań, czy teorii grafów. Niestety większość tego typu problemów stanowią pro-

blemy NP-trudne, których złożoność obliczeniowa rośnie wykładniczo, wraz ze wzrostem liczby danych

wejściowych. Powoduje to, że dla większości tego typu zagadnień jesteśmy zmuszeni do zastosowania al-

gorytmów aproksymacyjnych, zwracających przybliżone rozwiązanie problemu w rozsądnym czasie. Do

algorytmów aproksymacyjnych należą m.in. optymalizacja rojem cząstek, symulowane wyżarzanie, czy

algorytmy genetyczne.

## 4.1 Problem komiwojażera

Problem komiwojażera jest jednym ze znanych NP-trudnych problemów optymalizacji dyskretnej. Za-

gadnienie polega na znalezieniu najkrótszego cyklu w pełnym graﬁe ważonym, obejmującego wybrane

wierzchołki. Wierzchołki w takim graﬁe mogą reprezentować np. miasta, a wagi poszczególnych krawędzi

odległości między miastami.

W celu zobrazowania problemu wyobraźmy sobie graf z czterema wierzchołkami: A, B, C, D oraz

krawędziami, których wagi są przedstawione na Rysunku 4.1. Naszym zagadnieniem jest odnalezienie

najkrótszej ścieżki rozpoczynającej się w wierzchołku A i przechodzącej przez pozostałe trzy wierzchołki:

B, C, D. Musimy tutaj rozważyć następujące możliwości:

![obraz](https://user-images.githubusercontent.com/72522808/167308139-a4cec0f9-b7bb-4f1f-8b55-bc9179fb2d3e.png)


\1. A → C → B → D → A: 97

\2. A → C → B → D → A: 108

\3. A → C → B → D → A: 141

\4. A → C → D → B → A: 108

\5. A → D → B → C → A: 141

\6. A → D → C → B → A: 97

Jak widzimy najkrótsza w tym przykładzie okazała się ścieżka: A → B → C → D → A (oraz jej

symetryczne odbicie), której kosz wynosi: 97.

Złożoności najlepszego algorytmu dokładnego rozwiązującego problem komiwojażera wynosi: O(n22n),

gdzie n oznacza liczbę rozważanych wierzchołków. Jak widzimy czas działania algorytmu rośnie wykładni-

czo wraz ze w zrostem liczby rozważanych wierzchołków, co czyni go niepraktycznym już dla stosunkowo

niewielkich n.

## 4.2 Algorytm genetyczny

Algorytmy genetyczne czerpią swoją inspiracje z biologicznego procesu doboru naturalnego. W ramach

kolejnych iteracji (zwanych generacjami), algorytm genetyczny próbuje znaleźć optymalne rozwiązanie

dla zadanego problemu, poprzez łączenie ze sobą dotychczasowy rozwiązań.

Zanim przejdziemy do szczegółowego omówienia algorytmu, zdeﬁniujmy kilka pojęć wykorzystywanych

przez algorytmy genetyczne w kontekście problemu komiwojażera:

• Gen – pojedynczy wierzchołek w graﬁe.

• Osobnik – ścieżka łącząca wszystkie wierzchołki w graﬁe.

• Populacja – zbiór możliwych ścieżek (zbiór osobników).

• Rodzice – dwie ścieżki wykorzystywane do stworzenia nowej ścieżki.

Pojedyncza iteracja algorytmu genetycznego składa się z następujących kroków:

\1. Selekcja – wybranie najlepszych osobników z danej populacji jako rodziców następnego pokolenia.

\2. Krzyżowanie – łączenie ze sobą losowo wybranych rodziców w celu utworzenia nowych osobników stanowiących kolejną generację.

\3. Mutacja – wprowadzenie drobnych losowych zmian do nowo powstałej populacji.

Działanie algorytmu rozpoczyna się od wylosowania pierwszego pokolenia osobników, a następnie wy-

konywana jest zadana liczba iteracji. Najlepszy osobnik z ostatniej generacji stanowi rozwiązanie zadanego

problemu. Liczba iteracji oraz wielkość pojedynczej populacji są parametrami algorytmu.

Często w celu uzyskania lepszych parametrów algorytmu stosuje się tzw. strategie z częściową repro-

dukcją. Najpopularniejszym podejściem jest elityzm, w którym pewna liczba najlepszych osobników z

danej populacji jest przenoszona bez zmian do kolejnej generacji.

### 4.2.1 Selekcja

Selekcja jest pierwszym etapem iteracji algorytmu genetycznego. W ramach tego kroku dokonujemy wy-

boru najlepiej przystosowanych osobników, którzy następnie zostaną wykorzystani w etapie krzyżowania.

Istnieje kilka możliwych sposobów dokonania selekcji. Jednym z nich jest metoda koła ruletki1.

W metodzie koła ruletki, prawdopodobieństwo wylosowania osobnika jako kandydata do krzyżowania

jest proporcjonalne do jego dopasowania. Im lepiej dopasowany jest osobnik, tym większa szansa na jego

wybór. W metodzie tej jeden osobnik może zostać wybrany więcej niż jeden raz.

W celu zastosowania metody koła ruletki do problemu komiwojażera, wygodnie jest przekształcić pro-

blem z minimalizacyjnego na maksymalizacyjny. W tym celu wystarczy odwrócić naszą funkcję dopaso-

wania:

![obraz](https://user-images.githubusercontent.com/72522808/167308206-9f5c6595-d949-4cca-9697-abbb639ede63.png)

Algorytm selekcji metodą koła ruletki dla problemu komiwojażera został przedstawiony poniżej (Al-

gorytm 1).

Algorytm 1 Algorytm selekcji metodą koła ruletki dla problemu komiwojażera. Zakładamy, że słownik

zachowuje kolejność dodawanych elementów.

![obraz](https://user-images.githubusercontent.com/72522808/167308265-17802ed2-b50d-43a3-a8fd-ce3a035d300a.png)

W ramach etapu selekcji można zastosować elityzm, wybierając od razu pierwsze N najlepszych osob-

ników niezależnie od wyników losowania.

### 4.2.2 Krzyżowanie

Etap krzyżowania polega na połączeniu cech dwóch losowo wybranych osobników w celu utworzenia

nowego osobnika potomnego. W przypadku problemu komiwojażera, w celu zachowania poprawności nowo

powstałej ścieżki (ścieżka musi stanowić listę wszystkich wierzchołków grafu, gdzie każdy z wierzchołków

musi wystąpić dokładnie raz), należy zastosować specjalny wariant krzyżowania, zwany krzyżowaniem

uporządkowanym.

Krzyżowanie uporządkowane najłatwiej wyjaśnić na przykładzie. Wyobraźmy sobie że chcemy skrzy-

żować dwa osobniki:

parent1 = [7, 1, 6, 0, 5, 9, 2, 4, 8, 3]

parent2 = [7, 1, 5, 9, 4, 3, 6, 2, 0, 8]

Pierwszym etapem naszego algorytmu jest wylosowanie fragmentu pierwszego rodzica, który następnie

zostanie przeniesiony do rodzica drugiego. Załóżmy że wylosowaliśmy następujący fragment:

slice = [5, 9, 2, 4]

Następnym krokiem jest usunięcie z rodzica drugiego wszystkich elementów znajdujących się w wylo-

sowanym fragmencie:

oﬀspring = [7, 1, 3, 6, 0, 8]

Ostatecznie wstawiamy wylosowany fragment w odpowiednie miejsce pierwszego rodzica, tak aby

liczba elementów znajdujących się za wylosowanym fragmentem pierwszego rodzica, była równa liczbie

elementów znajdujących się za fragmentem w rozwiązaniu potomnym:

oﬀspring = [7, 1, 3, 6, 5, 9, 2, 4, 0, 8]

Krzyżowanie osobników powtarzamy aż do zapełnienia całej nowej populacji (rozmiary populacji mu-

szą się zgadzać pomiędzy kolejnymi iteracjami algorytmu). Tak samo jak w przypadku selekcji możemy

tutaj wykorzystać elityzm i nie poddawać zmianom najlepszych osobników.

### 4.2.3 Mutacja

Ostatnim etapem algorytmu genetycznego jest mutacja. Etap ten polega na wprowadzeniu niewielkich

losowych zmian do wygenerowanego pokolenia potomnego. W problemie komiwojażera można zastoso-

wać metodę polegającą na zamianie miejscami dwóch losowych elementów. Prawdopodobieństwo z jakim

zmiana może zostać dokonana jest jednym z parametrów algorytmu. Algorytm 2 realizuje mutację poje-

dynczego osobnika.

Algorytm 2 Algorytm mutacji pojedynczego osobnika dla problemu komiwojażera.

![obraz](https://user-images.githubusercontent.com/72522808/167308285-14664af1-ea8f-4999-a66a-4257f3e18d3f.png)

