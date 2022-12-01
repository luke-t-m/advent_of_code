{-# LANGUAGE NoMonomorphismRestriction #-}
{-# LANGUAGE FlexibleContexts          #-}
{-# LANGUAGE TypeFamilies              #-}

import Diagrams.Prelude
import Diagrams.Backend.SVG.CmdLine


import Data.Char
import Data.List
import Data.List.Split


foldUp foldY pnt@(y,x) | y > foldY = ((foldY - (y - foldY)), x)
                 | otherwise = pnt

foldLeft foldX pnt@(y,x) | x > foldX = (y, (foldX - (x - foldX)))
                   | otherwise = pnt

conv (x:[y]) = (y,x)



fold "y" foldY pnts = nub (map (foldUp foldY) pnts)
fold "x" foldX pnts = nub (map (foldLeft foldX) pnts)

what pnts (y,x) | (y,x) `elem` pnts = 'X'
                | otherwise = '.'

folder :: [(Int,Int)] -> [(String,String)] -> [(Int,Int)]
folder pnts [] = pnts
folder pnts ((n,t):fs) = folder (fold t (read n) pnts) fs

main :: IO ()
main = do
 input <- readFile "input.txt"
 let u = map (conv . splitOn "=" . last . splitOn " ") (lines (last (splitOn "\n\n" input)))
 let i = head (splitOn "\n\n" input)
 let points = map (conv . (map read) . splitOn ",") (lines i) :: [(Int,Int)]
 

 let folded = folder points u
 flip atPoints (repeat (circle 0.2 # fc green)) $ map p2 $ [(1,1), (0,3), (-2,1), (-1,-4), (2,0)]



