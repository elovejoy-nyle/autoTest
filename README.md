<pre>
Automated HPC Tester Desing notes, and future reference material. 
The test rig uses a PLC to read and write IO.

HOW the heck is this thing going to run? 
  we seem to be thinking this will be an integration of NEOLSI, and the cart where 
  we are prototyping this board.

  Chaotic project is chaotic. 
#tests:
  see HPC/PLC/:
       --> PLC testing components
  
  will organize later.

  
#Dependencies:
https://github.com/Makerspace-Bangor/fc6a/blob/main/src/MiSmSerial.py
python3
https://github.com/mitchsowa/esp-dual-loader
  
Platform:
  Well, this depends on the actual integration, thats still a mystery I guess.
  if you want it to do the PLCs, and the HPC, then we have to port some stuff to windows.
  if we use 2 computers. maybe one is linux and the other is windows.
(Im saying that there are windows dependent components I cant do much about right now )
  

#3D models for the board clamp:
  https://github.com/elovejoy-nyle/3D/blob/main/DIN_Clamp_long_side_stack.scad
#3D models for the DIN rails end caps:
  https://github.com/elovejoy-nyle/3D/blob/main/DIN_end_cap.scad

</pre>
