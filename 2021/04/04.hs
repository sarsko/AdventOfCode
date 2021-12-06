import Data.List.Split
import Data.List

commaNums :: String -> [Int]
commaNums = map read . splitOn ","

blend = zipWith (flip (++))

takeUntil _ [] = [];
takeUntil p (x:xs) = if p x then [x] else (x: takeUntil p xs)

removeNum inp idx = map (map (filter (/= idx))) inp

findBoard :: [Int] -> [Int] -> [[[Int]]] -> [[Int]]
findBoard negNeedle needle = head . filter f
    where
      f inp = notElem negNeedle inp && elem needle inp

parseInput input =
    blend inp $ map transpose inp
    where
        inp = chunksOf 5 $ map (map read . words) $ filter (not . null) $ tail input

main = do
    input <- lines <$> readFile "input.txt"
    let nums = commaNums $ head input
    let fin = parseInput input

    let s = scanl removeNum fin nums

    let res = takeUntil (any (any null)) s
    let num = nums!!(length res - 2)
    let part1 = findBoard [1337] [] $ last res
    print $ num * (sum $ map sum part1) `div` 2

    let res = takeWhile (not . (all (any null))) s
    let num = nums!!(length res - 1)
    let part2 = findBoard [] [num] $ last res
    print $ num * ((sum $ map sum part2) `div` 2 - num)
