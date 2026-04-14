from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Blog
from .serializers import BlogSerializer, UserSerializer


# ✅ Signup
@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


# 📄 Get all published blogs (public)
@api_view(['GET'])
@permission_classes([AllowAny])
def blog_list(request):
    blogs = Blog.objects.filter(status='published')
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)


# 📄 Blog detail (public)
@api_view(['GET'])
@permission_classes([AllowAny])
def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug, status='published')
    serializer = BlogSerializer(blog)
    return Response(serializer.data)


# ➕ Create blog (logged-in only)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_blog(request):
    serializer = BlogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(author=request.user)
        return Response(serializer.data)
    return Response(serializer.errors)


# ✏ Edit blog (only author)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_blog(request, id):
    blog = get_object_or_404(Blog, id=id)

    if blog.author != request.user:
        return Response({'error': 'Not allowed'}, status=403)

    serializer = BlogSerializer(blog, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


# 🗑 Delete blog (only author)
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_blog(request, id):
    blog = get_object_or_404(Blog, id=id)

    if blog.author != request.user:
        return Response({'error': 'Not allowed'}, status=403)

    blog.delete()
    return Response({'message': 'Deleted successfully'})


# 👤 Profile (own blogs)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):
    blogs = Blog.objects.filter(author=request.user)
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)