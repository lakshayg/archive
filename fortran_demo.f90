PROGRAM matrix_demo

  IMPLICIT NONE
  REAL, DIMENSION(3,3) :: X, Y, Z
  INTEGER :: I, J
  
  ! initialize the two matrices
  X = reshape((/1, 2, 3, 4, 5, 6, 7, 8, 9/), shape(X))
  Y = transpose(reshape((/1, 2, 3, 4, 5, 6, 7, 8, 9/), shape(Y)))

  WRITE (*,*) "X = "
  CALL DISPLAY(X, 3, 3)
  WRITE (*,*) "Y = "
  CALL DISPLAY(Y, 3, 3)
  Z = MATMUL(X,Y)
  WRITE (*,*) "Z = "
  CALL DISPLAY(Z, 3, 3)
  
END PROGRAM matrix_demo

SUBROUTINE DISPLAY(array, nrow, ncol)
  DIMENSION array(nrow,ncol)
  INTEGER :: I, J
  DO I=1,nrow
     WRITE(*,*) (array(I,J), J=1,ncol) ! implied loop
  END DO
END SUBROUTINE DISPLAY
