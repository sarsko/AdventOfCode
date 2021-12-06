import Data.List.Split
import Data.List

commaNums :: String -> [Int]
commaNums = map read . splitOn ","

oneDay [] = []
oneDay (x:xs)
    | x == 0 = 6:8:oneDay(xs)
    | otherwise = (x - 1):oneDay(xs)

main = do
    input <- commaNums <$> readFile "input.txt"
    let it = iterate oneDay input
    print $ length $ it!!80
    print $ length $ it!!256
