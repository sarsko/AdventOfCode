import Data.List.Split
import Data.List

commaNums :: String -> [Int]
commaNums = map read . splitOn ","

chunkify :: Int -> [x] -> [[x]]
chunkify n [] = []
chunkify n list = chunk : chunkify n rest
    where (chunk, rest) = splitAt n list

blend (x:xs) (y:ys) = (y++x):(blend ys xs)
blend _ _ = []

takeUntil _ [] = [];
takeUntil p (x:xs) = if p x then [x] else (x: takeUntil p xs)

removeNum inp idx =
    map (map (filter (\x -> x /= idx))) inp

findBoard negNeedle needle [] = []
findBoard negNeedle needle inp
    | (notElem negNeedle (inp!!0)) && (elem needle (inp!!0)) = inp!!0
    | otherwise = findBoard negNeedle needle $ tail inp

existsEmpty [] = False
existsEmpty inp
    | (any null) (inp!!0) = True
    | otherwise = existsEmpty $tail inp

allHasEmpty [] = True
allHasEmpty inp
    | elem [] $ inp!!0 = allHasEmpty $tail inp
    | otherwise = False

main = do
    input <- lines <$> readFile "input.txt"
    let nums = commaNums $ input!!0
    let inp = chunkify 5 $ map (map read . words) $ filter (not . null) $ tail input
    let fin = blend inp $ map transpose inp

    let s = scanl (removeNum) fin nums

    let res = takeUntil (existsEmpty) s
    let num = nums!!(length res - 2)
    let part1 = findBoard [1337] [] $ last res
    print $ num * (sum $ map sum part1) `div` 2

    let res = takeWhile (not . allHasEmpty) s
    let num = nums!!(length res - 1)
    let part2 = findBoard [] [num] $ last res
    print $ num * ((sum $ map sum part2) `div` 2 - num)

