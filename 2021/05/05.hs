{-# LANGUAGE TupleSections #-}
import Data.List.Split
import Data.List
import Control.Arrow

countElems inp = map (head &&& length) $ group $ sort inp

commaNums :: String -> [Int]
commaNums = map read . splitOn ","

toTuples [] = []
toTuples (x:y:xs) = (x,y):toTuples(xs)

removeDiags [] = []
removeDiags ((x,y):(x2,y2):xs)
    | x == x2 || y == y2  = (x,y):(x2,y2):removeDiags(xs)
    | otherwise = removeDiags(xs)

expand ((x,y):(x2,y2):xs)
    | x == x2 = map (x, ) [min y y2 .. max y y2]
    | y == y2 = map (, y) [min x x2 .. max x x2]
    | otherwise = zip (range x x2) (range y y2)
  where
      range x y
        | x < y = [x..y]
        | otherwise = [x,x-1..y]

main = do
    l <- lines <$> readFile "input.txt"
    let input = map (toTuples . commaNums) l
    let noDia = filter (not . null) $ map removeDiags input
    print $ length $ filter (\(x, y) -> y /= 1) $ countElems $ concat $ map expand noDia
    print $ length $ filter (\(x, y) -> y /= 1) $ countElems $ concat $ map expand input
