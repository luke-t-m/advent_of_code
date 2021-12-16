import Data.List
import Data.List.Split


plusone grid = map (map ((+) 1)) grid

cordCheck :: [[a]] -> (Int,Int) -> Bool
cordCheck grid (y,x) = y >= 0 && x >= 0 && y < lY && x < lX
 where
  lX = length (head grid)
  lY = length grid

--    0 1 2
--    3 x 4
--    5 6 7

mods = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]

applyMods (y,x) = map (\(y',x') -> (y+y',x+x')) mods

ninePosits grid = [(y,x) | y <- [0..length grid -1], x <- [0..length (head grid)-1], grid!!y!!x >= 9]

flash grid = chunksOf (length (head grid)) [ grid!!y!!x + (check (y,x)) | y <- [0..length grid -1], x <- [0..length (head grid)-1]]
 where
  check (y,x) | (y,x) `elem` (ninePosits grid) = -100000 -- hehe
              | otherwise = trues (map (\t -> t `elem` (ninePosits grid)) (applyMods (y,x)))

trues x = length (filter (==True) x)

stz grid = map (map zeroer) grid
 where zeroer x | x < 0 = 0
                | otherwise = x

flasher grid | stz (flash grid) == stz grid = grid
             | otherwise = flasher (flash grid)

step grid = stz (plusone (flasher grid))

stepper 0 grid flashes = flashes
stepper n grid flashes = stepper (n-1) (step grid) (flashes + (count0s (step grid)))

count0s grid = sum (map (length . filter (==0)) grid)

stepTillSyncFlash grid n | count0s grid == (length grid) * (length (head grid)) = n
                         | otherwise = stepTillSyncFlash (step grid) (n+1)

main :: IO ()
main = do
 input <- readFile "input.txt"
 let x = map ((map read) . tail . splitOn "") (lines input)
 print (stepper 100 x 0)   -- part 1
 print (stepTillSyncFlash x 0)  -- part 2
 print "done"
