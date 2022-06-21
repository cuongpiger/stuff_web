package entity

type Person struct {
	FirstName string `json:"firstname" binding:"required"`
	LastName  string `json:"lastname" binding:"required"`
	Age       int    `json:"age" binding:"gte=1,lte=130"`  // the age must be between 1 and 130
	Email     string `json:"email" validate:"required,email"`  // the email must be set and must be valid
}

type Video struct {
	Title       string `json:"title" binding:"min=2,max=10"`  // the length of the title must be between 2 and 10
	Description string `json:"description" binding:"max=20"`
	URL         string `json:"url" binding:"required,url"`  // the url must be specified and must be a valid url
	Author      string `json:"author" binding:"required"`  // the author must be specified
}
