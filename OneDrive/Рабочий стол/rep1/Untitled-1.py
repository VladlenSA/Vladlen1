<!DOCTYPE html>
<html>
<head>
    <title>Калькулятор BMI</title>
    <style>
        h1 {
            color: blue;
        }

        p {
            font-size: 18px;
            color: #333;
        }
    </style>
</head>
<body>
    <h1>Добро пожаловать в калькулятор BMI!</h1>
    <p>Введите ваш вес (кг) и рост (м) ниже, чтобы узнать ваш индекс массы тела.</p>
    
    <form action="" method="post">
        <label for="weight">Вес (кг):</label>
        <input type="text" name="weight" id="weight" required>
        
        <label for="height">Рост (м):</label>
        <input type="text" name="height" id="height" required>
        
        <input type="submit" value="Рассчитать BMI">
    </form>

    <h2>Результат:</h2>
    {% if bmi %}
        <p>Ваш индекс массы тела (BMI): {{ bmi|round(2) }}</p>
    {% else %}
        <p>Ошибка: введены некорректные данные!</p>
    {% endif %}
</body>
</html>
