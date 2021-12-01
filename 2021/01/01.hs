parse :: String -> [Int]
parse = map read . lines

solveA :: [Int] -> Int
solveA input = do
    -- (-1 +) $ length $ filter (\(x,y) -> x > y) $ zip input (-1 : input)
    length $ filter (\(x,y) -> x < y) $ zip input (tail input)

solveB :: [Int] -> Int
solveB input = do
    -- solveA $ drop 2 $ zipWith3 (\x y z -> x + y + z) input (0 : input) (0 : 0 : input)
    solveA $ zipWith3 (\x y z -> x + y + z) input (tail input) (drop 2 input)

main = do
    input <- parse <$> readFile "input.txt"
    print $ solveA input
    print $ solveB input
