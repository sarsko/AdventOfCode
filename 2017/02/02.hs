solveA :: [[Int]] -> Int
solveA input = do
    sum $ map (\e -> maximum e - minimum e) input
    -- sum [maximum row - minimum row | row <- input]

solveB :: [[Int]] -> Int
solveB input = do
    sum $ map (\e -> head [ x `div` y | x <- e, y <- e, x `mod` y == 0 && x /= y]) input

main = do
    input <- map (map read . words) . lines <$> readFile "input.txt"
    print $ solveA input
    print $ solveB input
