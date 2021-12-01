import Data.Char

converge :: (a -> a -> Bool) -> [a] -> a
converge p (x:ys@(y:_))
    | p x y     = y
    | otherwise = converge p ys

solver [] = []
solver ([x]) = [x]
solver (x:y:xs)
    | isLower y && x == toUpper y = solver xs
    | isLower x && y == toUpper x = solver xs
    | otherwise = x : (solver $ y : xs)

full x = length $ converge (==) $ iterate solver x

pre inp o = filter (\x -> x /= o && x /= toUpper o) inp

main = do
    input <- readFile "input.txt"
    let l = init input
    print $ full l
    let alph = ['a' .. 'z']
    print $ map full (map (pre l) alph)
