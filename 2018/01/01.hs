import qualified Data.Set as Set

parse :: String -> [Int]
parse = map read . lines . filter (/= '+')

solveA :: [Int] -> Int
solveA input = do
    sum $ input

findDup [] s = error "no dup"
findDup (x:xs) s
    | x `Set.member` s = x
    | otherwise = findDup xs $ Set.insert x s

main = do
    input <- parse <$> readFile "input.txt"
    print $ solveA input
    let tmp = tail $ scanl (+) 0 $ cycle input
    print $ findDup tmp Set.empty
