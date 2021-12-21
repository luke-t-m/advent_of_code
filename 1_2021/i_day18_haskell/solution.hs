import Data.Char

data SnailNo = No Int | Pair (SnailNo) (SnailNo) deriving (Show,Eq)

parseSN ('[' : a) = Pair (parseSN b) (parseSN c)
 where (b,',':c) = splitl a 0 0
       splitl x p n | x!!p == ',' && n == 0 = splitAt p x
                    | x!!p == '[' = splitl x (p+1) (n+1)
                    | x!!p == ']' = splitl x (p+1) (n-1)
                    | otherwise = splitl x (p+1) n
parseSN x = No (read (filter isDigit x))

explodeM (Pair (No a) (No b)) 4 = Pair (No (a*100)) (No (b*100))
explodeM (Pair a b) d | (explodeM a (d+1)) /= a = Pair (explodeM a (d+1)) b
                     | otherwise = Pair a (explodeM b (d+1))
explodeM x _ = x

findEML (Pair (No a) (No b)) | a >= 100 = a `div` 100
                             | otherwise = 0
findEML (Pair a b) = (findEML a) + (findEML b)
findEML x = 0

findEMR (Pair (No a) (No b)) | b >= 100 = b `div` 100
                             | otherwise = 0
findEMR (Pair a b) = (findEMR a) + (findEMR b)
findEMR x = 0

findGL (Pair a b) = findGL a
findGL (No a) = a < 100

findGR (Pair a b) = findGR b
findGR (No a) = a < 100

explodeL x@(Pair a b) n | findEML a /= 0 = Pair (explodeL a n) b
                        | findGL b = Pair a (explodeL b n)
                        | not (findGL b) = Pair (explodeL a (findEML b)) b
explodeL (No a) n | a >= 100 = No a
                  | otherwise = No (a+n)

explodeR x@(Pair a b) n | findEMR b /= 0 = Pair a (explodeR b n)
                        | findGR a = Pair (explodeR a n) b
                        | not (findGR a) = Pair a (explodeR b (findEMR a))
explodeR (No a) n | a >= 100 = No a
                  | otherwise = No (a+n)

fixEM x@(Pair (No a) (No b)) | a >= 100 || b >= 100 = No 0
                             | otherwise = x
fixEM (Pair a b) = Pair (fixEM a) (fixEM b)
fixEM x = x

explode a = fixEM (explodeR (explodeL (explodeM a 0) 0) 0)

split' x@(Pair a b) | split' a /= a = Pair (split' a) b
                    | split' b /= b = Pair a (split' b)
                    | otherwise = x
split' (No a) | a >= 10 = Pair (No (floor h)) (No (ceiling h))
              | otherwise = No a
 where h = (fromIntegral a) / 2

reduce a | explode a /= a = reduce (explode a)
         | split' a /= a = reduce (split' a)
         | otherwise = a

add a b = reduce (Pair (reduce a) (reduce b))

addAll x = foldl add (head x) (tail x)

magn (Pair a b) = 3 * (magn a) + 2 * (magn b)
magn (No a) = a

maxMagn x = maximum [ magn ((x!!n) `add` (x!!m)) | n <- [0..(length x)-1], m <- [0..(length x)-1]]

main :: IO ()
main = do
 input <- readFile "input.txt"
 let x = map parseSN (lines input)
 putStr "Part 1: "
 print (magn (addAll x))
 putStr "Part 2: "
 print (maxMagn x)
 print "done."
