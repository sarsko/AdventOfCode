-- From https://github.com/sondresl/AdventOfCode/blob/master/2021/Haskell/src/Lib.hs
binToInt :: String -> Int
binToInt = foldl (\acc new -> acc * 2 + new) 0 . map (read . pure)

filterIdx inp c idx =
    filter (\x -> x!!idx == c) inp

convert [] tresh c alt = []
convert (x:xs) tresh c alt
    | x > tresh = c : convert xs tresh c alt
    | otherwise = alt : convert xs tresh c alt

solveA inp =
    (binToInt $ convert counts half '0' '1') *
    (binToInt $ convert counts half '1' '0')
    where
        counts = map (length . filterIdx inp '0') [0..(-1 +) . length $ inp!!0]
        half = length inp `div` 2

oneIt cmp inp idx
    | length inp == 1 = inp
    | (length $ zeros) `cmp` (length $ ones) = zeros
    | otherwise = ones
    where
        zeros = filterIdx inp '0' idx
        ones = filterIdx inp '1' idx

solveB inp =
    (binToInt $ (foldl (oneIt (>)) inp range)!!0) *
    (binToInt $ (foldl (oneIt (<=)) inp range)!!0)
    where
        range = [0..(-1 +) $ length $ inp!!0]

main = do
    input <- lines <$> readFile "input.txt"
    print $ solveA input
    print $ solveB input
