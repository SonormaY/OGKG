int N = 10; 
int totalPoints = 4 * N; 
float R = 500; 
PVector[] points = new PVector[totalPoints]; 
int[] fibonacciNumbers;

void setup() {
  size(600, 600);

  // Центр квадрата
  float cx = width / 2;
  float cy = height / 2;

  // Відстань між точками
  float segmentLength = R / N;
  
  // Генерація точок на сторонах квадрата
  for (int i = 0; i < totalPoints; i++) {
    if (i < N) {
      points[i] = new PVector(cx - R/2 + i * segmentLength, cy - R/2); // Верхня сторона
    } else if (i < 2 * N) {
      points[i] = new PVector(cx + R/2, cy - R/2 + (i - N) * segmentLength); // Права сторона
    } else if (i < 3 * N) {
      points[i] = new PVector(cx + R/2 - (i - 2 * N) * segmentLength, cy + R/2); // Нижня сторона
    } else {
      points[i] = new PVector(cx - R/2, cy + R/2 - (i - 3 * N) * segmentLength); // Ліва сторона
    }
  }
  
  // Генеруємо числа Фібоначчі, менші ніж 4N
  fibonacciNumbers = generateFibonacci(totalPoints);
  
  // Малюємо точки
  for (PVector p : points) {
    ellipse(p.x, p.y, 5, 5);
  }

  // З'єднуємо точки згідно з правилом
  for (int i = 0; i < totalPoints; i++) {
    for (int f : fibonacciNumbers) {
      int j = (i + f) % totalPoints;
      line(points[i].x, points[i].y, points[j].x, points[j].y);
    }
  }
}

// Функція для генерації чисел Фібоначчі, менших за limit
int[] generateFibonacci(int limit) {
  ArrayList<Integer> fib = new ArrayList<Integer>();
  fib.add(1);
  fib.add(2);
  
  int a = 1, b = 2;
  while (b < limit) {
    int next = a + b;
    if (next >= limit) break;
    fib.add(next);
    a = b;
    b = next;
  }
  
  // Конвертуємо список у масив
  int[] result = new int[fib.size()];
  for (int i = 0; i < fib.size(); i++) {
    result[i] = fib.get(i);
  }
  return result;
}
