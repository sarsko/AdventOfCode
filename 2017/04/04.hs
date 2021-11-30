import qualified Data.Set as Set
import Data.Map (toList, fromListWith)

convert :: (Ord a) => [a] -> [(a, Int)]
convert xs = toList . fromListWith (+) . zip xs $ repeat 1

noDuplicates :: (Ord a) => [a] -> Bool
noDuplicates list = length list == length set
    where set = Set.fromList list

solve input = do
    length $ filter (\e -> noDuplicates e) input

main = do
    input <- map words . lines <$> readFile "input.txt"
    print $ solve input
    input2 <- map (map convert . words) . lines <$> readFile "input.txt"
    print $ solve input2
